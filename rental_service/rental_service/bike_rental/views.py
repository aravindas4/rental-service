from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
from rest_framework.throttling import ScopedRateThrottle
# Create your views here.
from bike_rental.models import Station, Rent
from bike_rental.serializers import StationSerializer, RentSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    throttle_scope = 'stations'
    throttle_classes = (ScopedRateThrottle,)
    filter_fields = (
        'name','latitude','longitude',
        )
    search_fields = (
        '^name',
        )
    ordering_fields = (
        'name',
        )

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    throttle_scope = 'rents'
    throttle_classes = (ScopedRateThrottle,)
    filter_fields = (
       'origin_station','destination_station','startdate','enddate',
       )
    search_fields = (
       '^origin_station','^destination_station',
       )
    ordering_fields = (
       'origin_station','destination_station','startdate','enddate',
       )
