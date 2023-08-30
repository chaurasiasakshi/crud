from django.db import models

# Create your models here.

class crud(models.Model):
    name = models.CharField(max_length=255)
    email=models.EmailField(max_length=254)
    address = models.CharField(max_length=255)
    age = models.PositiveBigIntegerField()
    photo = models.ImageField( upload_to='images/%Y/%m/%d/',max_length=255)
    