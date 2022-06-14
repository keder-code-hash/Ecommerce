from django.db import models
from .NamedModel import NamedModel


class DiscountModel(NamedModel):
    discount_amount = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    class Meta :
        db_table = "Discount"