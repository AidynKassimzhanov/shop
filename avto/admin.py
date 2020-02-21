from django.contrib import admin
from .models import Avto, BrandCar, ModelCar, Body, Volume

admin.site.register(Avto)
admin.site.register(BrandCar)
admin.site.register(ModelCar)
admin.site.register(Body)
admin.site.register(Volume)