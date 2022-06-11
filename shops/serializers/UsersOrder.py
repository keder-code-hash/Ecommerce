from ..models.UserOrders import UserOrder,OrderMeasureModel
from .NamedModel import BaseNamedModelSerializers
from .ProductModel import ProductModelSerializers,MeasuringModelSerializers
from ..models.UserOrders import OrderMeasureModel
from users.serializers.Users import UsersSerializers
from users.serializers.Address import AddressSerializers


class OrderMeasureModelSerializers(BaseNamedModelSerializers):
    ordered_prod = ProductModelSerializers()
    measure_params = MeasuringModelSerializers(many = True)
    class Meta:
        model = OrderMeasureModel
        fields = "__all__"


class UserOrderSerializers(BaseNamedModelSerializers):
    user = UsersSerializers()
    address = AddressSerializers()
    ordered_prod = OrderMeasureModelSerializers(many = True)
    class Meta :
        model = UserOrder
        fields = "__all__"