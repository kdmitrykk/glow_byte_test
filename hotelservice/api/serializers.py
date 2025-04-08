from datetime import date

from rest_framework import serializers

from reservations.models import HotelModel, ReservationModel


class ReservationSerializer(serializers.ModelSerializer):
    """Сериализатор для бронирования."""

    hotelUid = serializers.UUIDField(source='hotel.hotelUid')
    startDate = serializers.DateField()
    endDate = serializers.DateField()

    def validate_hotelUid(self, value):
        """Валидация на наличие отеля."""
        if not HotelModel.objects.filter(hotelUid=value).exists():
            raise serializers.ValidationError("Такого отеля не существует.")
        return value

    def validate(self, data):
        """Валидация для даты."""
        if data['startDate'] >= data['endDate']:
            raise serializers.ValidationError(
                "Дата начала бронирования должна быть раньше даты конца.")
        if data['startDate'] < date.today():
            raise serializers.ValidationError(
                "Дата начала бронирования не может быть в прошлом."
            )
        return data

    class Meta:
        """Вспомогательный класс Meta."""

        model = ReservationModel
        fields = ['reservationUid', 'hotelUid',
                  'startDate', 'endDate']
