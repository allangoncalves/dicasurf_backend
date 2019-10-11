from rest_framework import serializers
from api.models import *

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        exclude = ("preview_image", "preview_text")

class PostPreviewSerializer(serializers.ModelSerializer):
    preview_image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        exclude = ('text', 'image')

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        exclude = ('spot',)

class SpotDetailSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(read_only=True, many=True)
    header_image = ImageSerializer(many=False, read_only=True)
    info_image = ImageSerializer(many=False, read_only=True)

    class Meta:
        model = SpotDetail
        exclude = ('spot',)

class SpotSerializer(serializers.ModelSerializer):
    details = SpotDetailSerializer(read_only=True, many=False)

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