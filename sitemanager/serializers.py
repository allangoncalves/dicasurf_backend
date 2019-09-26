from rest_framework import serializers
from sitemanager.models import *

class SlideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slide
        fields = "__all__"


class HomePageSerializer(serializers.ModelSerializer):
    carousel = SlideSerializer(many=True)

    class Meta:
        model = HomePage
        fields = '__all__'
