from django.contrib import admin

from reservations.models import HotelModel, ReservationModel, LoyaltyModel


@admin.register(HotelModel)
class HotelAdmin(admin.ModelAdmin):
    """Админка для отелей."""

    list_display = ('hotelUid', 'name', 'address', 'price_for_nigth')
    search_fields = ('name', 'address')
    list_filter = ('price_for_nigth',)
    ordering = ('name',)


@admin.register(LoyaltyModel)
class LoyaltyAdmin(admin.ModelAdmin):
    """Админка для лояльности."""

    list_display = ('username',
                    'status',
                    'total_reservations')
    search_fields = ('username',)
    list_filter = ('status',)
    ordering = ('-total_reservations',)
    actions = ['reset_status']


@admin.register(ReservationModel)
class ReservationAdmin(admin.ModelAdmin):
    """Админка для бронирований."""

    list_display = (
        'reservationUid',
        'username',
        'hotel_info',
        'status',
        'startDate',
        'endDate',
        'nights_count',
        'amount'
    )
    list_filter = ('status', 'startDate')
    search_fields = ('username', 'reservationUid')
    raw_id_fields = ('hotel',)

    def hotel_info(self, obj):
        """Поле информации об отеле."""
        return f"{obj.hotel.name} ({obj.hotel.price_for_nigth}/night)"
    hotel_info.short_description = 'Hotel'

    def nights_count(self, obj):
        """Поле для количества ночей."""
        return (obj.endDate - obj.startDate).days
    nights_count.short_description = 'Nights'
