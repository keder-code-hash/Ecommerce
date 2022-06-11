from rest_framework import serializers
from ..models.ProductModel import ProductCountableModel,ProductMeasurableModel,ProductModel,MeasuringModel
from users.serializers.BaseModel import BaseModelSerializers
from ..models.PouchModel import PouchModel
from .PouchModel import PouchModelSerializers
from .NamedModel import BaseNamedModelSerializers
from .TagModel import TagModelSerializers

MEASURING_UNIT_CHOICES = [
    ('CT', 'Countable Quantity'),
    ('MS', 'Measurable Quantity') 
]
class ProductMeasurableModelSerializers(BaseModelSerializers): 
    pouch_details = PouchModelSerializers()
    class Meta : 
        model = ProductMeasurableModel
        fields = "__all__"

class ProductCountableModelSerializers(BaseModelSerializers): 
    class Meta : 
        model = ProductCountableModel
        fields = "__all__"

class MeasuringModelSerializers(BaseModelSerializers): 
    countable_product = ProductCountableModelSerializers(many = True)
    measurable_product = ProductMeasurableModelSerializers(many = True)


    class Meta :
        model = MeasuringModel
        fields = "__all__"



class ProductModelSerializers(BaseNamedModelSerializers): 
    measuring_params = MeasuringModelSerializers() 
    related_tags = TagModelSerializers(many = True) 
    class Meta : 
        model = ProductModel
        fields = "__all__"