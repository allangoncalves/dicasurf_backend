from django.db import models

# Create your models here.

BEACH_TYPE = (
    ('public', 'Pública'),
    ('private', 'Privada'),
)

CROWDS = (
    ('few', 'Poucos Surfistas'),
    ('many', 'Muitos Surfistas'),
)

WAVE_LENGTHS = (
    ('short', 'Curta'),
    ('long', 'Longa'),
    ('normal', 'Normal'),
)

WAVE_STRENGTH = (
    ('powerful', 'Potente'),
    ('soft', 'Suave'),
)


class Spot(models.Model):
    name = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    car = models.BooleanField(default=False)
    special_access = models.BooleanField(default=False)
    beach_type = models.CharField(max_length=100, choices=BEACH_TYPE)
    access_comment = models.TextField()
    time_of_year = models.TextField()
    good_day_description = models.TextField()
    week_crowd = models.CharField(max_length=50, blank=False, choices=CROWDS)
    weekend_crowd = models.CharField(max_length=50, blank=False, choices=CROWDS)
    wave_quality = models.IntegerField()
    wave_length = models.CharField(max_length=10, blank=False, choices=WAVE_LENGTHS)
    strength = models.CharField(max_length=10, blank=False, choices=WAVE_STRENGTH)

class AccessPoint(models.Model):
    stairwell = models.BooleanField(default=False)
    cliff = models.BooleanField(default=False)
    bay = models.BooleanField(default=False)
    trail = models.BooleanField(default=False)
    other = models.CharField(max_length=220, default="", blank=True)
    spot = models.ForeignKey(Spot, related_name='accesses', on_delete=models.CASCADE)

class GroundPoint(models.Model):
    rock = models.BooleanField(default=False)
    sand = models.BooleanField(default=False)
    coral = models.BooleanField(default=False)
    spot = models.ForeignKey(Spot, related_name='grounds', on_delete=models.CASCADE)

class BestTideMoves(models.Model):
    low = models.BooleanField(default=False)
    high = models.BooleanField(default=False)
    ebb = models.BooleanField(default=False)
    flood = models.BooleanField(default=False)
    spot = models.ForeignKey(Spot, related_name='best_tide_moves', on_delete=models.CASCADE)

class WaveDirection(models.Model):
    right = models.BooleanField(default=False)
    left = models.BooleanField(default=False)
    spot = models.ForeignKey(Spot, related_name='wave_directions', on_delete=models.CASCADE)