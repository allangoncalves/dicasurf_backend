from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from api.serializers import *

# Create your views here.

class SpotViewSet(viewsets.ModelViewSet):
    serializer_class = SpotSerializer

    def get_queryset(self):
        return Spot.objects.filter(city=self.kwargs['city_pk'])

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer

    def get_queryset(self):
        return City.objects.filter(state=self.kwargs['state_pk'])

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes] 
