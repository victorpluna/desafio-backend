from django.urls import path
from .views import TripListAPIView, TripRatingUpdateAPIView


urlpatterns = [
    path(
        '',
        TripListAPIView.as_view(),
        name='trips-list'
    ),
    path(
        '<int:pk>/',
        TripRatingUpdateAPIView.as_view(),
        name='trip-update-rating'
    ),
]