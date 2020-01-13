from rest_framework import serializers
from api.models import *

class PossiblePartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PossiblePartner
        fields = '__all__'

class FirstUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = FirstUser
        fields = '__all__'

class SphereVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SphereVideo
        fields = '__all__'

class SphereImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SphereImage
        fields = '__all__'

class VideoGridSerializer(serializers.ModelSerializer):
    video_one = SphereVideoSerializer(many=False, read_only=True)
    video_two = SphereVideoSerializer(many=False, read_only=True)
    video_three = SphereVideoSerializer(many=False, read_only=True)
    video_four = SphereVideoSerializer(many=False, read_only=True)
    video_five = SphereVideoSerializer(many=False, read_only=True)
    video_six = SphereVideoSerializer(many=False, read_only=True)

    class Meta:
        model = VideoGrid
        exclude = ('spot',)

class ImageGridSerializer(serializers.ModelSerializer):
    image_one = SphereImageSerializer(many=False, read_only=True)
    image_two = SphereImageSerializer(many=False, read_only=True)
    image_three = SphereImageSerializer(many=False, read_only=True)
    image_four = SphereImageSerializer(many=False, read_only=True)
    image_five = SphereImageSerializer(many=False, read_only=True)
    image_six = SphereImageSerializer(many=False, read_only=True)

    class Meta:
        model = ImageGrid
        exclude = ('spot',)
    

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
    pictures_gallery = ImageSerializer(many=False, read_only=True)
    videos_gallery = ImageSerializer(many=False, read_only=True)
    image_panel = serializers.SerializerMethodField()
    video_panel = serializers.SerializerMethodField()
    spot = SpotSerializer(many=False, read_only=True)

    class Meta:
        model = SpotDetail
        fields = "__all__"
        # exclude = ('spot',)

    def get_image_panel(self, instance):
        panels = instance.image_panel.all().order_by('id')
        return ImageGridSerializer(panels, many=True).data

    def get_video_panel(self, instance):
        panels = instance.video_panel.all().order_by('id')
        return ImageGridSerializer(panels, many=True).data

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