from django.db import models
from shops.models.NamedModel import NamedModel
from .OrderedItems import OrderedItems
from users.models.Users import Users,UserAddressModel
from .OrderedItems import OrderedItems


class OrderedDetails(NamedModel):
    ordered_items = models.OneToOneField(OrderedItems,on_delete=models.CASECADE,blank= True)
    total_amount  = models.IntegerField()
    ordered_by = models.ManyToManyField(Users)
    ordered_address = models.ManyToManyField(UserAddressModel)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_tables = "Ordered Details"
        abstract = False