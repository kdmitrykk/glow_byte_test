from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ReservationViewSet

router = DefaultRouter()
router.register('api/reservations', ReservationViewSet,
                basename='reservation')


urlpatterns = [
    path('hotelservice/', include(router.urls)),
]
