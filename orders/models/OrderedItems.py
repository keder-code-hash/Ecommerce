from django.db import models
from shops.models.NamedModel import NamedModel
from shops.models.Product_count_map import ProductCountModels

class OrderedItems(NamedModel):
    ordered_item_count = models.ManyToManyField(ProductCountModels)
    ordered_items_num = models.IntegerField()


    def __str__(self) -> str:
        return self.name
    class Meta: 
        db_table = "OrderedItems"
        abstract = False

        