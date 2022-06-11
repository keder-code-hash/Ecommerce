from rest_framework import serializers
from ..models.TagModel import Tagmodel
from .NamedModel import BaseNamedModelSerializers

class TagModelSerializers(BaseNamedModelSerializers):
    class Meta :
        model = Tagmodel
        fields = "__all__"

