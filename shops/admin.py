from django.contrib import admin
from .models.ProductModel import *
from .models.NamedModel import *
from .models.PouchModel import *
from .models.ShopModel import *
from .models.UserOrders import UserOrder,OrderMeasureModel
from .models.CartModel import CartModel
# Register your models here.

admin.site.register(ProductModel)
admin.site.register(MeasuringModel)
admin.site.register(ProductCountableModel)
admin.site.register(ProductMeasurableModel)

admin.site.register(PouchModel)

admin.site.register(ShopModel)

admin.site.register(CartModel)
admin.site.register(UserOrder)
admin.site.register(OrderMeasureModel)

