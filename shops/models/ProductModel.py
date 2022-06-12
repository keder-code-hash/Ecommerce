from django.db import models
from .NamedModel import BaseNamedmodel
from .PouchModel import validate_amount,PouchModel
from users.models.BaseModel import BaseModel
from .TagModel import Tagmodel

MEASURING_UNIT_CHOICES = [
    ('CT', 'Countable Quantity'),
    ('MS', 'Measurable Quantity') 
]
PROUDCT_MEASURING_CHOICE = [
    ('CM','COUNTABLE PRODUCT'),
    ('MM','MEASURING PRODUCT'),
    ('SC','SIMPLE COUNTABLE PRODUCT')
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
    measuring_choices = models.CharField(
                            max_length=2,
                            choices=PROUDCT_MEASURING_CHOICE,
                            default="SC"
                        )
    measuring_params = models.OneToOneField(MeasuringModel,on_delete=models.CASCADE,blank=True)
    related_tags = models.ManyToManyField(Tagmodel,verbose_name="tags according to product",related_name="tags_product",blank=True)

    class Meta : 
        # abstract = False
        db_table = "Product"