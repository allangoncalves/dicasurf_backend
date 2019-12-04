from rest_framework import serializers
from api.models import *

class FirstUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = FirstUser
        fields = '__all__'

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
        exclude = ('text',)

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        exclude = ('spot',)

class SpotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spot
        fields = '__all__'

class SpotDetailSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(read_only=True, many=True)
    header_image = ImageSerializer(many=False, read_only=True)
    info_image = ImageSerializer(many=False, read_only=True)
    spot = SpotSerializer(many=False, read_only=True)

    class Meta:
        model = SpotDetail
        fields = "__all__"
        # exclude = ('spot',)

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