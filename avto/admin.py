from django.contrib import admin
from .models import Avto, BrandCar, ModelCar, Body, Volume, Categories, Product

admin.site.register(Avto)
admin.site.register(BrandCar)
admin.site.register(ModelCar)
admin.site.register(Body)
admin.site.register(Volume)
admin.site.register(Categories)
admin.site.register(Product)