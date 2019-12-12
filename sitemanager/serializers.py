from rest_framework import serializers
from api.serializers import ImageSerializer
from sitemanager.models import *

class SlideSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)
    
    class Meta:
        model = Slide
        fields = "__all__"

class PartnerSlideSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartnerSlide
        fields = "__all__"

class WhoWeAreSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoWeAreSlide
        fields = "__all__"

class WhoWeArePageSerializer(serializers.ModelSerializer):
    carousel = WhoWeAreSlideSerializer(many=True)
    
    class Meta:
        model = WhoWeArePage
        fields = "__all__"

class PartnerPageSerializer(serializers.ModelSerializer):
    carousel = PartnerSlideSerializer(many=True)
    
    class Meta:
        model = PartnerPage
        fields = "__all__"

class HomePageSerializer(serializers.ModelSerializer):
    carousel = SlideSerializer(many=True)

    class Meta:
        model = HomePage
        fields = '__all__'


