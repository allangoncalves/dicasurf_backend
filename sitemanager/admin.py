from django.contrib import admin
from sitemanager.models import *

# Register your models here.


class CarouselInline(admin.StackedInline):
    model = Slide

class HomeAdmin(admin.ModelAdmin):
    inlines = [CarouselInline]

class PartnerInline(admin.StackedInline):
    model = PartnerSlide

class PartnerAdmin(admin.ModelAdmin):
    inlines = [PartnerInline]

class WhoWeAreInline(admin.StackedInline):
    model = WhoWeAreSlide

class WhoWeAreAdmin(admin.ModelAdmin):
    inlines = [WhoWeAreInline]

admin.site.register(HomePage, HomeAdmin)
admin.site.register(PartnerPage, PartnerAdmin)
admin.site.register(WhoWeArePage, WhoWeAreAdmin)
admin.site.register(SphereImage)
admin.site.register(Image)
