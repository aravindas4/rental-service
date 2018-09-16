import pytest
from datetime import datetime
# import django
# if hasattr(django, 'setup'):
#     django.setup()
from django.test import TestCase
from bike_rental.models import Station, Rent
from mixer.backend.django import mixer
#from

@pytest.mark.django_db
class TestStation(TestCase):
    def setUp(self):
        self.initial_count = Station.objects.all().count()
        self.city1 = mixer.blend('bike_rental.Station',name="C2422", latitude = 8311, longitude = 98, bike_available_quantity=34)

    def test_data_creation1(self):
        final_count = Station.objects.all().count()
        diff = final_count - self.initial_count
        assert diff == 1
        assert self.city1.__str__() == "C2422"

    def tearDown(self):
        self.city1.delete()

@pytest.mark.django_db
class TestRent(TestCase):
    def setUp(self):
        self.initial_count = Rent.objects.all().count()
        self.city1 = mixer.blend('bike_rental.Station',name="C223", latitude = 313, longitude = 100, bike_available_quantity=34)
        self.c1bikes = self.city1.bike_available_quantity

        self.city2 = mixer.blend('bike_rental.Station',name="C221", latitude = 312, longitude = 99, bike_available_quantity=34)
        self.c2bikes = self.city2.bike_available_quantity

        self.rent = mixer.blend('bike_rental.Rent',origin_station=self.city1, destination_station = self.city2, startdate = datetime.now())
        self.final_count = Rent.objects.all().count()

    def tearDown(self):
        if self.rent:
            self.rent.delete()
        self.city1.delete()
        self.city2.delete()


    def test_data_creation2(self):
        # intial_count = Rent.objects.all().count()
        # city1 = mixer.blend('bike_rental.Station',name="C122", latitude = 311, longitude = 98, bike_available_quantity=34)
        # city2 = mixer.blend('bike_rental.Station',name="G122", latitude = 761, longitude = 948, bike_available_quantity=34)
        # o_bikes = self.city1.bike_available_quantity
        # d_bikes = self.city2.bike_available_quantity
        # r = mixer.blend('bike_rental.Rent',origin_station=city1, destination_station = city2, startdate = datetime.now())
        # final_count = Rent.objects.all().count()
        diff = self.final_count - self.initial_count
        assert diff == 1
        assert self.rent.is_active == True
        assert self.c1bikes-1 == self.city1.bike_available_quantity
        # r.delete()
        # city1.delete()
        # city2.delete()

    def test_data_updating(self):
        # city1 = mixer.blend('bike_rental.Station',name="C73", latitude = 491, longitude = 98, bike_available_quantity=34)
        # city2 = mixer.blend('bike_rental.Station',name="G73", latitude = 411, longitude = 948, bike_available_quantity=34)
        # o_bikes = self.city1.bike_available_quantity
        # d_bikes = self.city2.bike_available_quantity
        # r = mixer.blend('bike_rental.Rent',origin_station=city1, destination_station = city2, startdate = datetime.now())
        self.rent.enddate = datetime.now()
        self.rent.save()
        assert self.rent.is_active == False
        assert self.c2bikes+1 == self.city2.bike_available_quantity
        # r.delete()
        # city1.delete()
        # city2.delete()

    def test_data_updating2(self):
        # city1 = mixer.blend('bike_rental.Station',name="C6", latitude = 10, longitude = 98, bike_available_quantity=34)
        # city2 =  mixer.blend('bike_rental.Station',name="G6", latitude = 16, longitude = 948, bike_available_quantity=34)
        # o_bikes = self.city1.bike_available_quantity
        # d_bikes = self.city2.bike_available_quantity
        # r = mixer.blend('bike_rental.Rent',origin_station=city1, destination_station = city2, startdate = datetime.now())
        self.rent.delete()
        assert self.c1bikes == self.city1.bike_available_quantity
        assert self.rent.is_active == False
        # city1.delete()
        # city2.delete()
