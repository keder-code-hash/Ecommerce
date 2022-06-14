from django.db import models

from .NamedModel import NamedModel
from .UserOrders import OrderMeasureModel

from users.models.Users import Users
from .Product_count_map import ProductCountModels

class CartModel(NamedModel):

    product_count_map = models.ForeignKey(ProductCountModels,on_delete=models.CASCADE,blank=True)
    Users = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,related_name="users_cart")

    def __str__(self) -> str:
        return self.name

    class Meta :
        ordering = ['created_at']
        abstract = False


