from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from api.serializers import ReservationSerializer
from reservations.models import HotelModel, LoyaltyModel, ReservationModel


class ReservationViewSet(mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    """ViewSet для управления бронированиями."""

    queryset = ReservationModel.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        """Создание объекта бронирования."""

        username = request.headers.get('X-User-Name')
        if not username:
            return Response(
                {"error": "Добавьте идентификатор пользователя."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        loyalty, _ = LoyaltyModel.objects.get_or_create(username=username)

        hotel = HotelModel.objects.get(
            hotelUid=serializer.validated_data['hotel']['hotelUid'])
        startDate = serializer.validated_data['startDate']
        endDate = serializer.validated_data['endDate']
        nights = (endDate - startDate).days

        base_price = nights * hotel.price_for_nigth
        discount = {'BRONZE': 0.05,
                    'SILVER': 0.07,
                    'GOLD': 0.10
                    }.get(loyalty.status, 0)
        total_amount = base_price * (1 - discount)

        reservation = ReservationModel.objects.create(
            username=loyalty,
            hotel=hotel,
            startDate=startDate,
            endDate=endDate,
            amount=total_amount
        )

        loyalty.total_reservations += 1
        self.update_loyalty_status(loyalty)
        loyalty.save()

        return Response(
            ReservationSerializer(reservation).data,
            status=status.HTTP_201_CREATED
        )

    def destroy(self, request, *args, **kwargs):
        """Удаление объетка бронирования."""
        username = request.headers.get('X-User-Name')
        if not username:
            return Response(
                {"error": "Добавьте идентификатор пользователя."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            reservation = self.get_object()
        except ReservationModel.DoesNotExist:
            return Response(
                {"error": "Такого бронирования нет."},
                status=status.HTTP_404_NOT_FOUND
            )

        if str(reservation.username) != username:
            return Response(
                {"error": "Вы не можете отменять чужие бронировая."},
                status=status.HTTP_403_FORBIDDEN
            )

        if reservation.status == ReservationModel.CANCELED:
            return Response(
                {"error": "Бронирование уже отменено."},
                status=status.HTTP_400_BAD_REQUEST
            )

        reservation.status = ReservationModel.CANCELED
        reservation.save()

        loyalty = LoyaltyModel.objects.get(username=username)
        loyalty.total_reservations = max(0, loyalty.total_reservations - 1)
        self.update_loyalty_status(loyalty)
        loyalty.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def update_loyalty_status(self, loyalty):
        if loyalty.total_reservations >= 20:
            loyalty.status = LoyaltyModel.GOLD
        elif loyalty.total_reservations >= 10:
            loyalty.status = LoyaltyModel.SILVER
        else:
            loyalty.status = LoyaltyModel.BRONZE
