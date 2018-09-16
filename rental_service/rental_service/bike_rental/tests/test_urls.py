from django.urls import reverse, resolve
from django.test import TestCase
from bike_rental.models import Station, Rent
from mixer.backend.django import mixer
from datetime import datetime

class TestUrls(TestCase):
    def setUp(self):
        #self.initial_count = Station.objects.all().count()
        self.city1 = mixer.blend('bike_rental.Station',name="C322", latitude = 3111, longitude = 98, bike_available_quantity=34)
        self.city2 = mixer.blend('bike_rental.Station',name="C221", latitude = 312, longitude = 99, bike_available_quantity=34)
        self.rent = mixer.blend('bike_rental.Rent',origin_station=self.city1, destination_station = self.city2, startdate = datetime.now())

    def test_station_detail_url(self):
        # s = mixer.blend('bike_rental.Station',name="New City120", latitude = 41, longitude = 88, bike_available_quantity=34)
        url = reverse('station-detail', kwargs={'pk':self.city1.id})
        assert resolve(url).view_name == 'station-detail'

    def test_rent_detail_url(self):
        # s = mixer.blend('bike_rental.Station',name="New City120", latitude = 41, longitude = 88, bike_available_quantity=34)
        url = reverse('rent-detail', kwargs={'pk':self.rent.id})
        assert resolve(url).view_name == 'rent-detail'

    def tearDown(self):
        self.rent.delete()
        self.city1.delete()
        self.city2.delete()
