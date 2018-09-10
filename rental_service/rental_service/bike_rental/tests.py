# import pytest
#
# import django
# if hasattr(django, 'setup'):
#     django.setup()
#
# from .models import Station
#
# import os, django
#
# @pytest.mark.django_db
# def test_data_creation():
#     intial_count = Station.objects.all().count()
#     s = Station(name="maahika2", latitude = 41, longitude = 45, bike_available_quantity=34)
#     s.save()
#     final_count = Station.objects.all().count()
#     diff = final_count - intial_count
#     assert diff == 1
