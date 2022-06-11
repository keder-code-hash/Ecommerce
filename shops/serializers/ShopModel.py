from rest_framework import serializers

from .ProductModel import ProductModelSerializers
from users.serializers.Users import UsersSerializers
from users.serializers.Address import AddressSerializers
from ..models.ShopModel import ShopModel

class ShopModelSerializers(serializers.ModelSerializer):
    shop_prouducts = ProductModelSerializers(many = True)
    shop_owner = UsersSerializers() 
    partners = UsersSerializers() 
    shop_address = AddressSerializers(many = True)  
    class Meta:
        model = ShopModel
        fields = "__all__"
