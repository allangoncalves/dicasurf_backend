from django.shortcuts import render
from sitemanager.serializers import *
from rest_framework.permissions import AllowAny
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework import viewsets

# Create your views here.
class HomePageViewSet(viewsets.ModelViewSet):
    serializer_class = HomePageSerializer
    queryset = HomePage.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]