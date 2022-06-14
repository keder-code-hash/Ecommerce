from rest_framework import serializers
from ..models.Discount import DiscountModel
from .NamedModel import NamedModelSerializers

class DiscountSerializers(NamedModelSerializers):
    class Meta:
        model = DiscountModel
        fields = "__all__"