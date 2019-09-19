from rest_framework import serializers
from api.models import *

class SpotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spot
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'