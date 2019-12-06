from django.db import models
from sitemanager.models import Image

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

PARTNERSHIP = (
    (1, 'Sunrise'),
    (2, 'Big Rider'),
    (3, 'Rosa dos Ventos'),
    (4, 'Adesão Anual'),
)

class PossiblePartner(models.Model):
    email = models.EmailField()
    choice = models.CharField(max_length=15, choices=PARTNERSHIP, null=False, blank=False)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Possiveis Parceiros"
    
    def __str__(self):
        return f'{self.email} - {self.choice}'

class FirstUser(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios pre-registrados"
    
    def __str__(self):
        return f'{self.email}'

class Post(models.Model):
    title = models.CharField("Título", max_length=140, blank=False)
    text = models.TextField("Texto")
    preview_text = models.TextField("Texto de preview", max_length=450, blank=False)
    preview_image = models.ForeignKey(Image, related_name="post_previews", on_delete=models.SET_NULL, verbose_name="Imagem de preview", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.created_at.date()}'

class State(models.Model):
    name = models.CharField("Nome do estado", max_length=100, blank=False)
    abbreviation = models.CharField("Sigla do estado", max_length=2, blank=False)
    is_visible = models.BooleanField("Visivel para todos", default=False)
    lat = models.FloatField("Latitude")
    lng = models.FloatField("Longitude")

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return f'{self.name} - {self.abbreviation}'

class City(models.Model):
    name = models.CharField("Nome da cidade", max_length=100, blank=False)
    state = models.ForeignKey(State, related_name="cities", on_delete=models.CASCADE, verbose_name="Estado",)
    is_visible = models.BooleanField("Visivel para todos", default=False)
    lat = models.FloatField("Latitude")
    lng = models.FloatField("Longitude")

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __str__(self):
        return f'{self.name}/{self.state.abbreviation}'

class Spot(models.Model):
    # General info
    name = models.CharField("Nome", max_length=100, blank=False)
    city = models.ForeignKey(City, related_name="spots", on_delete=models.CASCADE, verbose_name="Cidade",)
    lat = models.FloatField("Latitude")
    lng = models.FloatField("Longitude")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pico"
        verbose_name_plural = "Picos"

    def __str__(self):
        return f'{self.name} - {self.city}'

class SpotDetail(models.Model):
    spot = models.OneToOneField(Spot, related_name="details", on_delete=models.CASCADE, verbose_name="Pico",)
    # Images
    header_image = models.ForeignKey(Image, related_name="detail_headers", on_delete=models.SET_NULL, verbose_name="Imagem principal", null=True)
    info_image = models.ForeignKey(Image, related_name="detail_infos", on_delete=models.SET_NULL, verbose_name="Imagem lateral", null=True)
    # Accessibility
    car = models.BooleanField("Acesso de carro", default=False)
    special_access = models.BooleanField("Acesso especial", default=False)
    beach_type = models.CharField("Tipo de praia", max_length=100, choices=BEACH_TYPE)
    # Comments
    time_of_year = models.TextField("Melhor época do ano")
    good_day_description = models.TextField("Dia bom")
    access_comment = models.TextField("Comentário sobre o acesso")
    # Crowd
    week_crowd = models.CharField("Crowd na semana", max_length=50, blank=False, choices=CROWDS)
    weekend_crowd = models.CharField("Crowd no final de semana", max_length=50, blank=False, choices=CROWDS)
    # Wave info
    wave_quality = models.IntegerField("Qualidade das ondas")
    wave_length = models.CharField("Comprimento da onda", max_length=10, blank=False, choices=WAVE_LENGTHS)
    wave_strength = models.CharField("Força", max_length=10, blank=False, choices=WAVE_STRENGTH)
    # Acessess
    stairwell = models.BooleanField("Escadaria", default=False)
    cliff = models.BooleanField("Falésia", default=False)
    bay = models.BooleanField("Beira Mar", default=False)
    trail = models.BooleanField("Trilha", default=False)
    other_accesses = models.CharField("Outros acessos", max_length=220, default="", blank=True)
    # Grounds
    rock = models.BooleanField("Pedra", default=False)
    sand = models.BooleanField("Areia", default=False)
    coral = models.BooleanField("Coral", default=False)
    # Best tide moves
    low = models.BooleanField("Seca", default=False)
    high = models.BooleanField("Cheia", default=False)
    ebb = models.BooleanField("Secando", default=False)
    flood = models.BooleanField("Enchendo", default=False)
    # Wave directions
    right = models.BooleanField("Direita", default=False)
    left = models.BooleanField("Esquerda", default=False)
    # Surf Levels
    beginner = models.BooleanField("Iniciante", default=False)
    intermediate = models.BooleanField("Intermediário", default=False)
    expert = models.BooleanField("Experiente", default=False)
    # Wave frequency
    low_frequency = models.BooleanField("Frequência baixa", default=False)
    regular_frequency = models.BooleanField("Frequência regular", default=False)
    high_frequency = models.BooleanField("Frequência alta", default=False)
    # Dangers
    current = models.BooleanField("Correnteza", default=False)
    localism = models.BooleanField("Localismo", default=False)
    boat = models.BooleanField("Barcos", default=False)
    jetski = models.BooleanField("Jet Ski", default=False)
    buoy = models.BooleanField("Bóias", default=False)
    pollution = models.BooleanField("Poluição", default=False)
    rocks = models.BooleanField("Pedras", default=False)
    shark = models.BooleanField("Tubarões", default=False)
    undertow = models.BooleanField("Ressaca", default=False)
    other_dangers = models.CharField("Outros perigos", max_length=220, default="", blank=True)

    class Meta:
        verbose_name = "Pico do DicaSurf"
        verbose_name_plural = "Picos do DicaSurf"
    
    def __str__(self):
        return self.spot.name

class Video(models.Model):
    spot = models.ForeignKey(SpotDetail, related_name="videos", on_delete=models.CASCADE, verbose_name="Detalhamento",)
    title = models.CharField("Título breve", max_length=100, blank=False)
    thumb_image = models.ForeignKey(Image, related_name="videos", on_delete=models.SET_NULL, verbose_name="Arquivo thumb", null=True)
    youtube_url = models.URLField("Link do youtube")
    
    class Meta:
        verbose_name = "Vídeo"
        verbose_name_plural = "Vídeos"

    def __str__(self):
        return f'{self.spot} - {self.title}'
