from django.utils.http import urlencode
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from bike_rental.models import Station, Rent
from bike_rental import views
from mixer.backend.django import mixer
from django.urls import reverse
from datetime import datetime

class StationTests(APITestCase):
    @classmethod
    def setUpClass(self):
        #self.view = views.StationViewSet.as_view({'get': 'list'})
        super().setUpClass()
        self.uri = '/stations/'
        self.client = APIClient()


    @classmethod
    def tearDownClass(self):
        #self.client.quit()
        super().tearDownClass()

    def setUp(self):
        self.data =  {'name':'Other city New',
                    'latitude':87,
                    'longitude':9108,
                    'bike_available_quantity':90}
        self.city1 = mixer.blend('bike_rental.Station',name="C223", latitude = 313, longitude = 100, bike_available_quantity=34)

    def tearDown(self):
        #station = Station.objects.filter(name = self.data['name']).first()
        self.city1.delete()

    def test_station_list(self):
        response = self.client.get(self.uri)
        assert response.status_code == 200

    def test_station_detail(self):
        response = self.client.get(self.uri, {'pk':self.city1.id})
        assert response.status_code == 200

    def test_station_creation(self):
        data =  {'name':'Other city2',
                    'latitude':971,
                    'longitude':908,
                    'bike_available_quantity':90}
        response = self.client.post(self.uri, data)
        assert response.status_code == 201
        Station.objects.all().order_by('-id').first().delete()

    def test_station_creation2(self):
        data =  {'name':'Other city2',
                    'latitude':971,
                    'longitude':908,
                    'bike_available_quantity':90}
        response = self.client.post(self.uri, data)
        response = self.client.post(self.uri, data)
        assert response.status_code == 400
        Station.objects.all().order_by('-id').first().delete()

        def test_station_creation2(self):
            data =  {'name':'Other city245',
                        'latitude':971,
                        'longitude':908,
                        'bike_available_quantity':90}
            response = self.client.post(self.uri, data)
            response = self.client.post(self.uri, data)
            assert response.status_code == 400
            Station.objects.all().order_by('-id').first().delete()

class RentTests(APITestCase):
    @classmethod
    def setUpClass(self):
        #self.view = views.StationViewSet.as_view({'get': 'list'})
        super().setUpClass()
        self.uri = '/rents/'
        self.client = APIClient()


    @classmethod
    def tearDownClass(self):
        #self.client.quit()
        super().tearDownClass()

    def setUp(self):

        self.city1 = mixer.blend('bike_rental.Station',name="C223", latitude = 313, longitude = 100, bike_available_quantity=34)
        self.city2 = mixer.blend('bike_rental.Station',name="C221", latitude = 312, longitude = 99, bike_available_quantity=34)
        self.data =  {'origin_station':self.city1,
                    'destination_station':self.city2,
                    'startdate':datetime.now()}
        self.rent = mixer.blend('bike_rental.Rent',origin_station=self.city1, destination_station = self.city2, startdate = datetime.now())

    def tearDown(self):
        self.rent.delete()

    def test_rent_list(self):
        response = self.client.get(self.uri)
        assert response.status_code == 200

    def test_rent_detail(self):
        response = self.client.get(self.uri, {'pk':self.rent.id})
        assert response.status_code == 200

    def test_rent_creation(self):
        # data =  {'origin_station':self.city1,
        #             'destination_station':self.city2,
        #             'longitude':9108,
        #             'bike_available_quantity':90}
        response = self.client.post(self.uri, self.data)
        assert response.status_code == 201
        Rent.objects.all().order_by('-id').first().delete()

    def test_rent_updating(self):
        response = self.client.patch(self.uri, {'pk':self.rent.id, 'enddate':datetime.now()})
        assert response.status_code == 201
        Rent.objects.all().order_by('-id').first().delete()
