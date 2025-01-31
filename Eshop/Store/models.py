from django.db import models
from .category import Category
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='Uploads/products/')


