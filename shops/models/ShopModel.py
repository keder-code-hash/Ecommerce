from django.db import models

# from users.models.Address import Address
from .NamedModel import NamedModel
from .ProductModel import ProductModel
from users.models.Users import UserAddressModel,Users
from .Product_count_map import ProductCountModels

class ShopModel(NamedModel):
    shop_prouducts = models.ForeignKey(ProductCountModels,on_delete=models.CASCADE,blank=True)
    shop_owner = models.OneToOneField(Users,blank=False,on_delete=models.CASCADE,related_name="shop_owner",verbose_name="owner of the shop")
    partners = models.ManyToManyField(Users,blank=True,related_name="partners",verbose_name="partners of Shop")
    shop_address = models.ManyToManyField(UserAddressModel,blank=True,related_name="shop_address",verbose_name="shop address")
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = "Shop"
