from django.db import models

from .NamedModel import NamedModel
from .UserOrders import OrderMeasureModel

from users.models.Users import Users

class CartModel(NamedModel):

    cart_product = models.ManyToManyField(OrderMeasureModel,related_name="items_in_cart",blank=True)
    product_count = models.IntegerField()
    Users = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,related_name="users_cart")

    def __str__(self) -> str:
        return self.name

    class Meta :
        ordering = ['created_at']
        abstract = False


