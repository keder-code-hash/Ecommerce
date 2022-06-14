from django.db import models

from shops.models.Discount import DiscountModel
from .NamedModel import NamedModel
from .TagModel import Tagmodel
 
PROUDCT_MEASURING_CHOICE = [
    ('CM','COUNTABLE PRODUCT'),
    ('MM','MEASURABLE PRODUCT'),
    ('SC','SIMPLE COUNTABLE PRODUCT')
]
AMOUNT_UNIT_CHOICES = [
    ('KG', 'KiloGram'),
    ('GR', 'Gram'),
    ('LT', 'Litre'),
    ('KL', 'KiloLitre'),
    ('CT','NORMAL COUNTABLE')
]

class ProductModel(NamedModel):
    product_images = models.ImageField(upload_to = 'images/') # width and height set, validators add
    tags = models.ManyToManyField(Tagmodel,related_name="tags_product",blank=True,null=True)

    product_measuring_choices = models.CharField(
                            max_length=2,
                            choices=PROUDCT_MEASURING_CHOICE,
                            default="SC"
                        )
    price_of_product_single_unit = models.IntegerField()
    discount = models.ForeignKey(DiscountModel,on_delete=models.CASCADE,blank=True,null=True)
    product_measure_unit = models.CharField(
                            max_length=2,
                            choices=AMOUNT_UNIT_CHOICES,
                            default="CT"
                        )   

    class Meta : 
        db_table = "Product"

    def __str__(self) -> str:
        return self.name