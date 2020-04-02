from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import TripSerializer


class TripListAPIView(ListAPIView):
    serializer_class = TripSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return self.request.user.trips.all().order_by('-start_date')
