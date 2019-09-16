from django.contrib import admin

# Register your models here.

from api.models import *


admin.site.register(State)
admin.site.register(City)
admin.site.register(Spot)

