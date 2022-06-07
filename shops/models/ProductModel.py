from django.db import models
from .NamedModel import BaseNamedmodel
from .PouchModel import validate_amount,PouchModel
from users.models.BaseModel import BaseModel

MEASURING_UNIT_CHOICES = [
    ('CT', 'Countable Quantity'),
    ('MS', 'Measurable Quantity') 
]
class ProductMeasurableModel(BaseModel):
    prices = models.IntegerField(validators=[validate_amount])
    quantity_count = models.IntegerField(validators=[validate_amount])
    pouch_details = models.OneToOneField(PouchModel,on_delete=models.CASCADE)
    class Meta : 
        abstract = False

class ProductCountableModel(BaseModel):
    prices = models.IntegerField(validators=[validate_amount])
    quantity_count = models.IntegerField(validators=[validate_amount]) 
    class Meta : 
        abstract = False

class MeasuringModel(BaseModel):
    measuring_unit = models.CharField(
                        max_length=2,
                        choices=MEASURING_UNIT_CHOICES,
                        default="CT",
                    )
    countable_product = models.ManyToManyField(ProductCountableModel,blank=True)
    measurable_product = models.ManyToManyField(ProductMeasurableModel,blank=True)

    class Meta :
        # abstract = True
        # ordering = []
        pass



class ProductModel(BaseNamedmodel):
    product_images = models.ImageField(upload_to = 'images/') # width and height set, validators add
    measuring_params = models.OneToOneField(MeasuringModel,on_delete=models.CASCADE)
    class Meta : 
        # abstract = False
        db_table = "Product"