from django.db import models
from .NamedModel import NamedModel


class DiscountModel(NamedModel):
    discount_amount = models.IntegerField()
    
    class Meta :
        db_table = "Discount"