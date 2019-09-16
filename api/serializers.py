from rest_framework import serializers
from api.models import *

class DangersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dangers
        exclude = ('id',)

class AccessPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessPoint
        exclude = ('id',)

class GroundPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroundPoint
        exclude = ('id',)

class BestTideMovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestTideMoves
        exclude = ('id',)

class WaveDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaveDirection
        exclude = ('id',)

class SurfLevelNeededSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurfLevelNeeded
        exclude = ('id',)

class WaveFrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = WaveFrequency
        exclude = ('id',)

class SpotSerializer(serializers.ModelSerializer):
    accesses = AccessPointSerializer()
    grounds = GroundPointSerializer()
    best_tide_moves = BestTideMovesSerializer()
    wave_directions = WaveDirectionSerializer()
    surf_levels = SurfLevelNeededSerializer()
    wave_frequencies = WaveFrequencySerializer()
    dangers = DangersSerializer()

    class Meta:
        model = Spot
        fields = '__all__'

    def create(self, validated_data):
        accesses_data = validated_data.pop('accesses')
        accesses = AccessPoint.objects.create(**accesses_data)
        grounds_data = validated_data.pop('grounds')
        grounds = GroundPoint.objects.create(**grounds_data)
        best_tide_moves_data = validated_data.pop('best_tide_moves')
        best_tide_moves = BestTideMoves.objects.create(**best_tide_moves_data)
        wave_directions_data = validated_data.pop('wave_directions')
        wave_directions = WaveDirection.objects.create(**wave_directions_data)
        surf_levels_data = validated_data.pop('surf_levels')
        surf_levels = SurfLevelNeeded.objects.create(**surf_levels_data)
        wave_frequencies_data = validated_data.pop('wave_frequencies')
        wave_frequencies = WaveFrequency.objects.create(**wave_frequencies_data)
        dangers_data = validated_data.pop('dangers')
        dangers = Dangers.objects.create(**dangers_data)

        spot = Spot.objects.create(
            accesses=accesses,
            grounds=grounds,
            best_tide_moves=best_tide_moves,
            wave_directions=wave_directions,
            surf_levels=surf_levels,
            wave_frequencies=wave_frequencies,
            dangers=dangers,
            **validated_data
        )
        return spot

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'