from rest_framework import serializers
from ..models.Discount import DiscountModel

class DiscountSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiscountModel
        fields = "__all__"