from rest_framework import serializers
from api.serializers import ImageSerializer
from sitemanager.models import *

class SlideSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)
    
    class Meta:
        model = Slide
        fields = "__all__"


class HomePageSerializer(serializers.ModelSerializer):
    carousel = SlideSerializer(many=True)

    class Meta:
        model = HomePage
        fields = '__all__'
