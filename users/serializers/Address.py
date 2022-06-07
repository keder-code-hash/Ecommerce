from .BaseModel import BaseModelSerializers
from ..models.Users import UserAddressModel

class AddressSerializers(BaseModelSerializers):
 
    class Meta:
        model = UserAddressModel
        fields = "__all__"

 