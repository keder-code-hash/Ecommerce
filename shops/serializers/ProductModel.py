from rest_framework import serializers 
from .Discount import DiscountSerializers
from .NamedModel import BaseNamedModelSerializers
from .TagModel import TagModelSerializers
from ..models.ProductModel import ProductModel
 

class ProductModelSerializers(BaseNamedModelSerializers): 
    discount = DiscountSerializers()
    tags = TagModelSerializers(many = True) 
    class Meta : 
        model = ProductModel
        fields = "__all__" 