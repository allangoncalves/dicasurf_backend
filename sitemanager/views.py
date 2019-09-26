from django.shortcuts import render
from sitemanager.serializers import *
from rest_framework import viewsets

# Create your views here.
class HomePageViewSet(viewsets.ModelViewSet):
    serializer_class = HomePageSerializer
    queryset = HomePage.objects.all()