from rest_framework.serializers import ModelSerializer
from ..models.PouchModel import PouchModel

class PouchModelSerializers(ModelSerializer):
    class Meta : 
        model = PouchModel
        fields = "__all__"