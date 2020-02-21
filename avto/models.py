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

class Categories(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='children', blank=True)
        
    def __str__(self):
        return '%s, %s' % (self.parent, self.name)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    name = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField()
    category = models.ForeignKey('Categories', verbose_name="категория товара", on_delete=models.SET_NULL, null=True)
    avto = models.ManyToManyField('Avto')
    count = models.PositiveSmallIntegerField("количество в наличии", default=0)
    data = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_new = models.PositiveSmallIntegerField(default=0)
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автозапчасти"
        verbose_name_plural = "Список запчастей"