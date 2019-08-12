from rest_framework import viewsets
from api.serializers import *

# Create your views here.

class SpotViewSet(viewsets.ModelViewSet):
    serializer_class = SpotSerializer

    def get_queryset(self):
        return Spot.objects.filter(city=self.kwargs['city_pk'])

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer

    def get_queryset(self):
        return City.objects.filter(state=self.kwargs['state_pk'])

class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
