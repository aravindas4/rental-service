import pytest
from datetime import datetime
# import django
# if hasattr(django, 'setup'):
#     django.setup()
from bike_rental.models import Station, Rent
from mixer.backend.django import mixer
#from
@pytest.mark.django_db
class TestStation:

    def test_data_creation1(self):
        intial_count = Station.objects.all().count()
        s = mixer.blend('bike_rental.Station',name="New City120", latitude = 41, longitude = 88, bike_available_quantity=34)
        final_count = Station.objects.all().count()
        diff = final_count - intial_count
        assert diff == 1
        assert s.__str__() == "New City120"
        s.delete()

@pytest.mark.django_db
class TestRent:
    def test_data_creation2(self):
        intial_count = Rent.objects.all().count()
        city1 = mixer.blend('bike_rental.Station',name="C122", latitude = 311, longitude = 98, bike_available_quantity=34)
        city2 = mixer.blend('bike_rental.Station',name="G122", latitude = 761, longitude = 948, bike_available_quantity=34)
        o_bikes = city1.bike_available_quantity
        d_bikes = city2.bike_available_quantity
        r = mixer.blend('bike_rental.Rent',origin_station=city1, destination_station = city2, startdate = datetime.now())
        final_count = Rent.objects.all().count()
        diff = final_count - intial_count
        assert diff == 1
        assert r.is_active == True
        assert o_bikes-1 == city1.bike_available_quantity
        r.delete()
        city1.delete()
        city2.delete()

    def test_data_updating(self):
        city1 = mixer.blend('bike_rental.Station',name="C73", latitude = 491, longitude = 98, bike_available_quantity=34)
        city2 = mixer.blend('bike_rental.Station',name="G73", latitude = 411, longitude = 948, bike_available_quantity=34)
        o_bikes = city1.bike_available_quantity
        d_bikes = city2.bike_available_quantity
        r = mixer.blend('bike_rental.Rent',origin_station=city1, destination_station = city2, startdate = datetime.now())
        r.enddate = datetime.now()
        r.save()
        assert r.is_active == False
        assert d_bikes+1 == city2.bike_available_quantity
        r.delete()
        city1.delete()
        city2.delete()

    def test_data_updating2(self):
        city1 = mixer.blend('bike_rental.Station',name="C6", latitude = 10, longitude = 98, bike_available_quantity=34)
        city2 =  mixer.blend('bike_rental.Station',name="G6", latitude = 16, longitude = 948, bike_available_quantity=34)
        o_bikes = city1.bike_available_quantity
        d_bikes = city2.bike_available_quantity
        r = mixer.blend('bike_rental.Rent',origin_station=city1, destination_station = city2, startdate = datetime.now())
        r.delete()
        assert o_bikes == city1.bike_available_quantity
        assert r.is_active == False
        city1.delete()
        city2.delete()
