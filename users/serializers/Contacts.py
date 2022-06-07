
from .BaseModel import BaseModelSerializers

from ..models.Contacts import Contact

class ContactSerializers(BaseModelSerializers):
     
    class Meta:
        model = Contact
        fields = "__all__"