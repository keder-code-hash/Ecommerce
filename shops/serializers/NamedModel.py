from ..models.NamedModel import BaseModel,BaseNamedmodel
from rest_framework import serializers

class BaseNamedModelSerializers(serializers.ModelSerializer):
    class Meta: 
        model = BaseNamedmodel
        fields = "__all__"

class BaseModelSerializers(serializers.ModelSerializer):
    class Meta : 
        model = BaseModel
        fields = "__all__"