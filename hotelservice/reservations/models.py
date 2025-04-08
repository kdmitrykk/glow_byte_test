import uuid

from django.db import models


class HotelModel(models.Model):
    """Модель для отелей."""

    hotelUid = models.UUIDField('Идентификатор',
                                primary_key=True,
                                default=uuid.uuid4,
                                editable=False)
    name = models.CharField('Название',
                            max_length=256)
    address = models.CharField('Полный адрес',
                               max_length=256)
    price_for_nigth = models.PositiveIntegerField('Стоимость за ночь')

    class Meta:
        """Специальный класс Meta."""

        verbose_name = 'отель'
        verbose_name_plural = 'Отели'
        ordering = ['-price_for_nigth',
                    'name']

    def __str__(self):
        """Информация о модели."""
        return self.name


class LoyaltyModel(models.Model):
    """Модель для программы лояльности."""

    BRONZE = 'BRONZE'
    SILVER = 'SILVER'
    GOLD = 'GOLD'

    STATUS = [
        (BRONZE, 'Bronze'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
    ]

    username = models.CharField('Имя пользователя',
                                primary_key=True,
                                max_length=256)
    total_reservations = models.PositiveIntegerField('Число бронирований',
                                                     default=0)
    status = models.CharField('Статус лояльности',
                              choices=STATUS,
                              default='BRONZE',
                              max_length=10)

    class Meta:
        """Специальный класс Meta."""

        verbose_name = 'программа лояльности'
        verbose_name_plural = 'Программы лояльности'

    def __str__(self):
        """Текстовое представление."""
        return self.username


class ReservationModel(models.Model):
    """Модель для бронирований."""

    SUCCESS = 'SUCCESS'
    CANCELED = 'CANСELED'

    STATUS = (
        (SUCCESS, 'Success'),
        (CANCELED, 'Canceled')
    )

    reservationUid = models.UUIDField('Идентификатор',
                                      primary_key=True,
                                      default=uuid.uuid4,
                                      editable=False)
    username = models.ForeignKey(LoyaltyModel,
                                 verbose_name='Имя пользователя.',
                                 on_delete=models.CASCADE)
    hotel = models.ForeignKey(HotelModel,
                              verbose_name='Название отеля',
                              on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS,
                              default='SUCCESS',
                              max_length=10,
                              verbose_name='Статус')
    startDate = models.DateField('Начало бронирования')
    endDate = models.DateField('Конец бронирования')
    amount = models.PositiveIntegerField('Сумма бронирования', default=0)

    class Meta:
        """Специальный класс Meta."""

        verbose_name = 'бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        """Текстовое представление."""
        return f'Бронирование {self.reservationUid} имеет статус {self.status}'
