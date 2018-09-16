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

    # def destroy(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     now = datetime.datetime.now()
    #     timediff = now - obj.startdate
    #     buffertime = 600
    #     if timediff > buffertime:
    #         return Response(data={'message': "Too late to delete"},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #     self.perform_destroy(obj)
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def partial_update(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     now = datetime.datetime.now()
    #     timediff = now - obj.startdate
    #     buffertime = 600
    #     if timediff > buffertime:
    #         return Response(data={'message': "Too late to change"},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #     #def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
