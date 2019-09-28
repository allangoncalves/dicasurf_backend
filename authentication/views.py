from django.shortcuts import render
from rest_framework import viewsets

from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser, AllowAny
from authentication.models import User
from authentication.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'retrieve':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'destroy' or self.action == 'list':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]