from django.urls import path
from .views import TripListAPIView


urlpatterns = [
    path(
        '',
        TripListAPIView.as_view(),
        name='trips-list'
    ),
]