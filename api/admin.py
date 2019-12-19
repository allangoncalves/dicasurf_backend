from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

from api.models import *

admin.site.site_header = "DicaSurf Admin"

class PossiblePartnerAdmin(admin.ModelAdmin):
    list_filter = ('choice',)

class VideoInline(admin.StackedInline):
    model = Video

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

class SpotAdmin(admin.ModelAdmin):
    list_filter = ('city__name',)
    fieldsets = (

        ('Cidade', {
            'fields': ('city',),
        }),
        ('Informaçōes Gerais', {
            'fields': ('name',),
        }),
        ('Coordenadas', {
            'fields': ('lat', 'lng',),
        }),
    )

class SpotDetailAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    fieldsets = (
        ('Pico', {
            'fields': ('spot',),
        }),
        ('Imagens para a pagina.', {
            'fields': ('header_image', 'pictures_gallery', 'videos_gallery'),
        }),
        ('Acessibilidade', {
            'fields': ('beach_type', ('car', 'special_access')),
        }),
        ('Acessos', {
            'fields': (('stairwell', 'cliff', 'bay', 'trail'), 'other_accesses',),
        }),
        ('Fundos', {
            'fields': (('rock', 'sand', 'coral'),),
        }),
        ('Melhores movimentos da maré', {
            'fields': (('low', 'high', 'ebb', 'flood'),),
        }),
        ('Comentários', {
            'fields': ('time_of_year', 'good_day_description', 'access_comment'),
        }),
        ('Crowd', {
            'fields': ('week_crowd', 'weekend_crowd'),
        }),
        ('Perigos', {
            'fields': (
                'current',
                'localism',
                'boat',
                'jetski',
                'buoy',
                'pollution',
                'rocks',
                'shark',
                'undertow',
                'other_dangers',
            ),
        }),
        ('Informações de onda', {
            'fields': ('wave_quality', 'wave_length', 'wave_strength'),
        }),
        ('Direção das ondas', {
            'fields': (('right', 'left'),),
        }),
        ('Niveis de surf', {
            'fields': (('beginner', 'intermediate', 'expert'),),
        }),
        ('Frequência das ondas', {
            'fields': (('low_frequency', 'regular_frequency', 'high_frequency'),),
        }),
    )

admin.site.register(State)
admin.site.register(City)
admin.site.register(Spot, SpotAdmin)
admin.site.register(SpotDetail, SpotDetailAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(FirstUser)
admin.site.register(ImageGrid)
admin.site.register(VideoGrid)
admin.site.register(PossiblePartner, PossiblePartnerAdmin)

