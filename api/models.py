from django.db import models

# Create your models here.

BEACH_TYPE = (
    ('Pública', 'Pública'),
    ('Privada', 'Privada'),
)

CROWDS = (
    ('Poucos Surfistas', 'Poucos Surfistas'),
    ('Muitos Surfistas', 'Muitos Surfistas'),
)

WAVE_LENGTHS = (
    ('Curta', 'Curta'),
    ('Longa', 'Longa'),
    ('Normal', 'Normal'),
)

WAVE_STRENGTH = (
    ('Potente', 'Potente'),
    ('Suave', 'Suave'),
)

class Dangers(models.Model):
    current = models.BooleanField(default=False)
    localism = models.BooleanField(default=False)
    boat = models.BooleanField(default=False)
    jetski = models.BooleanField(default=False)
    buoy = models.BooleanField(default=False)
    pollution = models.BooleanField(default=False)
    rock = models.BooleanField(default=False)
    shark = models.BooleanField(default=False)
    undertow = models.BooleanField(default=False)
    other = models.CharField(max_length=220, default="", blank=True)

class AccessPoint(models.Model):
    stairwell = models.BooleanField(default=False)
    cliff = models.BooleanField(default=False)
    bay = models.BooleanField(default=False)
    trail = models.BooleanField(default=False)
    other = models.CharField(max_length=220, default="", blank=True)

class GroundPoint(models.Model):
    rock = models.BooleanField(default=False)
    sand = models.BooleanField(default=False)
    coral = models.BooleanField(default=False)

class BestTideMoves(models.Model):
    low = models.BooleanField(default=False)
    high = models.BooleanField(default=False)
    ebb = models.BooleanField(default=False)
    flood = models.BooleanField(default=False)

class WaveDirection(models.Model):
    right = models.BooleanField(default=False)
    left = models.BooleanField(default=False)

class SurfLevelNeeded(models.Model):
    beginner = models.BooleanField(default=False)
    intermediate = models.BooleanField(default=False)
    expert = models.BooleanField(default=False)

class WaveFrequency(models.Model):
    low = models.BooleanField(default=False)
    regular = models.BooleanField(default=False)
    high = models.BooleanField(default=False)

class State(models.Model):
    name = models.CharField(max_length=100, blank=False)
    abbreviation = models.CharField(max_length=2, blank=False)

    def __str__(self):
        return f'{self.name} - {self.abbreviation}'

class City(models.Model):
    name = models.CharField(max_length=100, blank=False)
    state = models.ForeignKey(State, related_name="cities", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Spot(models.Model):
    name = models.CharField(max_length=100, blank=False)
    lat = models.FloatField()
    lng = models.FloatField()
    car = models.BooleanField(default=False)
    city = models.ForeignKey(City, related_name="spots", on_delete=models.CASCADE)
    special_access = models.BooleanField(default=False)
    beach_type = models.CharField(max_length=100, choices=BEACH_TYPE)
    access_comment = models.TextField()
    time_of_year = models.TextField()
    good_day_description = models.TextField()
    week_crowd = models.CharField(max_length=50, blank=False, choices=CROWDS)
    weekend_crowd = models.CharField(max_length=50, blank=False, choices=CROWDS)
    wave_quality = models.IntegerField()
    wave_length = models.CharField(max_length=10, blank=False, choices=WAVE_LENGTHS)
    wave_strength = models.CharField(max_length=10, blank=False, choices=WAVE_STRENGTH)
    accesses = models.OneToOneField(AccessPoint, on_delete=models.CASCADE)
    grounds = models.OneToOneField(GroundPoint, on_delete=models.CASCADE)
    best_tide_moves = models.OneToOneField(BestTideMoves, on_delete=models.CASCADE)
    wave_directions = models.OneToOneField(WaveDirection, on_delete=models.CASCADE)
    surf_levels = models.OneToOneField(SurfLevelNeeded, on_delete=models.CASCADE)
    wave_frequencies = models.OneToOneField(WaveFrequency, on_delete=models.CASCADE)
    dangers = models.OneToOneField(Dangers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'