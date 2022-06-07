from rest_framework import serializers
from ..models.BaseModel import BaseModel

class BaseModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = "__all__"