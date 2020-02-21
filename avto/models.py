from django.db import models

class Volume(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Объем двигателя"
        verbose_name_plural = "Список объемов двигателя"

class Body(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Кузовы"

class BrandCar(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Марка авто"
        verbose_name_plural = "Список автомобильных марок"

class ModelCar(models.Model):
    name = models.CharField(max_length=20)
    brandCar = models.ForeignKey(BrandCar, verbose_name="Тип авто", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Тип модели"
        verbose_name_plural = "список моделей"

class Avto(models.Model):
    brandCar = models.ForeignKey(BrandCar, verbose_name="Тип авто", on_delete=models.SET_NULL, null=True)
    modelCar = models.ForeignKey(ModelCar, verbose_name="Тип модели", on_delete=models.SET_NULL, null=True)
    body = models.ForeignKey(Body, verbose_name="Тип кузова", on_delete=models.SET_NULL, null=True)
    volume = models.ForeignKey(Volume, verbose_name="Объем двигателя", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return '%s %s, %s, %s' % (self.brandCar, self.modelCar, self.volume, self.body)
    
    class Meta:
        verbose_name = "Тип авто"
        verbose_name_plural = "Автомобили"