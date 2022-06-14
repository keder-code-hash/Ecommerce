from django.db import models
from .ProductModel import ProductModel

class ProductCountModels(models.Model):
    product = models.OneToOneField(ProductModel,on_delete=models.CASCADE,blank=True)
    count = models.IntegerField()

 
    class Meta:
        db_table = "ProductCount"