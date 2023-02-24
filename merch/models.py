from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/$d/")
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=255)

class Categories(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

class Cart(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()