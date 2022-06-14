from users.serializers.Users import UsersSerializers
from ..models.NamedModel import BaseModel,BaseNamedmodel,NamedModel
from rest_framework import serializers

class BaseModelSerializers(serializers.ModelSerializer): 
    class Meta : 
        model = BaseModel
        fields = "__all__"

class BaseNamedModelSerializers(BaseModelSerializers): 

    class Meta: 
        model = BaseNamedmodel
        fields = "__all__"

class NamedModelSerializers(BaseModelSerializers): 

    class Meta: 
        model = NamedModel
        fields = "__all__"


