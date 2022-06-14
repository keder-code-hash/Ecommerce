from rest_framework import serializers
from .ProductModel import ProductModelSerializers
from ..models.Product_count_map import ProductCountModels

class ProductCountModels(serializers.ModelSerializer):

    product = ProductModelSerializers()

    class Meta:
        model = ProductCountModels
        fields = "__all__"