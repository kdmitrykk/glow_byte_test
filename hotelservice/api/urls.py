from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ReservationViewSet

router_v1 = DefaultRouter()
router_v1.register('api/v1/reservations', ReservationViewSet,
                   basename='reservation')


urlpatterns = [
    path('hotelservice/', include(router_v1.urls)),
]
