from ..models.CartModel import CartModel
from .UsersOrder import OrderMeasureModelSerializers
from users.serializers.Users import UsersSerializers
from .NamedModel import BaseNamedModelSerializers

class CartMOdelSerializers(BaseNamedModelSerializers):

    card_product = OrderMeasureModelSerializers(many = True)
    Users = UsersSerializers(many = True)

    class Meta :
        model = CartModel
        fields = "__all__"