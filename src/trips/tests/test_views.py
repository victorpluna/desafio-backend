from datetime import datetime, timedelta

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from mixer.backend.django import mixer

from trips.models import Trip


class TripTestCase(APITestCase):
    def setUp(self):
        self.URL_LIST = reverse('trips-list')
        self.customer = mixer.blend('accounts.Customer')
        self.token = str(AccessToken.for_user(self.customer))

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {self.token}')

        self.trips = mixer.cycle(3).blend('trips.Trip', customer=self.customer)

    def test_trip_list_without_authentication_401(self):
        self.client.credentials()
        response = self.client.get(self.URL_LIST)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_trip_list_with_authentication_200(self):
        response = self.client.get(self.URL_LIST)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_trip_list_return_own_content(self):
        # Creates 2 trips to another customer
        mixer.cycle(2).blend('trips.Trip')

        response = self.client.get(self.URL_LIST)
        self.assertEqual(response.data.get('count'), 3)

    def test_trip_update_without_authetication_401(self):
        self.client.credentials()

        trip = mixer.blend('trips.Trip', customer=self.customer)

        payload = {
            'classificacao': Trip.Classification.RECREATION,
            'nota': 5
        }
        response = self.client.put(
            reverse('trip-update-rating', args=[trip.id]), payload
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_trip_update_with_authetication_201(self):
        trip = mixer.blend('trips.Trip', customer=self.customer)

        payload = {
            'classificacao': Trip.Classification.RECREATION,
            'nota': 5
        }
        response = self.client.put(
            reverse('trip-update-rating', args=[trip.id]), payload
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_trip_update_fields(self):
        trip = mixer.blend(
            'trips.Trip', customer=self.customer,
            rating=1, classification=Trip.Classification.WORK
        )

        new_classification = Trip.Classification.PHYSICAL_ACTIVITY
        new_rating = 5

        payload = {
            'classificacao': new_classification,
            'nota': new_rating
        }
        self.client.put(
            reverse('trip-update-rating', args=[trip.id]), payload
        )

        updated_trip = Trip.objects.get(id=trip.id)
        self.assertEqual(updated_trip.classification, new_classification)
        self.assertEqual(updated_trip.rating, new_rating)

    def test_trip_update_invalid_rating_400(self):
        trip = mixer.blend('trips.Trip', customer=self.customer)

        invalid_rating = 6

        payload = {
            'classificacao': Trip.Classification.PHYSICAL_ACTIVITY,
            'nota': invalid_rating
        }
        response = self.client.put(
            reverse('trip-update-rating', args=[trip.id]), payload
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_trip_update_invalid_classification_400(self):
        trip = mixer.blend('trips.Trip', customer=self.customer)

        invalid_classification = 8

        payload = {
            'classificacao': invalid_classification,
            'nota': 3
        }
        response = self.client.put(
            reverse('trip-update-rating', args=[trip.id]), payload
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_trip_update_another_customer_400(self):
        trip = mixer.blend('trips.Trip')

        payload = {
            'classificacao': Trip.Classification.WORK,
            'nota': 3
        }
        response = self.client.put(
            reverse('trip-update-rating', args=[trip.id]), payload
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
