from django.contrib import admin
from sitemanager.models import *

# Register your models here.


class CarouselInline(admin.StackedInline):
    model = Slide

class HomeAdmin(admin.ModelAdmin):
    inlines = [CarouselInline]

admin.site.register(HomePage, HomeAdmin)
