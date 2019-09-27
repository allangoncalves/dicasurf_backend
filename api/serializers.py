from rest_framework import serializers
from api.models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        exclude = ('spot',)

class SpotSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(read_only=True, many=True)

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

class CityAndStateSerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = City
        fields = "__all__"


class SpotAndCitySerializer(serializers.ModelSerializer):
    city = CityAndStateSerializer()

    class Meta:
        model = Spot
        fields = "__all__"