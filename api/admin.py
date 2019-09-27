from django.contrib import admin

# Register your models here.

from api.models import *

admin.site.site_header = "DicaSurf Admin"

class VideoInline(admin.StackedInline):
    model = Video

class SpotAdmin(admin.ModelAdmin):
    list_filter = ('city__name',)
    inlines = [VideoInline]
    fieldsets = (
        ('Informações gerais', {
            'fields': ('name', 'city', 'header_image', 'info_image'),
            'classes': ['collapse']
        }),
        ('Coordenadas', {
            'fields': ('lat', 'lng'),
            'classes': ['collapse']
        }),
        ('Acessibilidade', {
            'fields': ('beach_type', ('car', 'special_access')),
            'classes': ['collapse']
        }),
        ('Acessos', {
            'fields': (('stairwell', 'cliff', 'bay', 'trail'), 'other_accesses',),
            'classes': ['collapse']
        }),
        ('Fundos', {
            'fields': (('rock', 'sand', 'coral'),),
            'classes': ['collapse']
        }),
        ('Melhores movimentos da maré', {
            'fields': (('low', 'high', 'ebb', 'flood'),),
            'classes': ['collapse']
        }),
        ('Comentários', {
            'fields': ('time_of_year', 'good_day_description', 'access_comment'),
            'classes': ['collapse']
        }),
        ('Crowd', {
            'fields': ('week_crowd', 'weekend_crowd'),
            'classes': ['collapse']
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
            'classes': ['collapse']
        }),
        ('Informações de onda', {
            'fields': ('wave_quality', 'wave_length', 'wave_strength'),
            'classes': ['collapse']
        }),
        ('Direção das ondas', {
            'fields': (('right', 'left'),),
            'classes': ['collapse']
        }),
        ('Niveis de surf', {
            'fields': (('beginner', 'intermediate', 'expert'),),
            'classes': ['collapse']
        }),
        ('Frequência das ondas', {
            'fields': (('low_frequency', 'regular_frequency', 'high_frequency'),),
            'classes': ['collapse']
        }),
    )

admin.site.register(State)
admin.site.register(City)
admin.site.register(Spot, SpotAdmin)
admin.site.register(Post)

