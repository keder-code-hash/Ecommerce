from ..models.CartModel import CartModel
from users.serializers.Users import UsersSerializers
from .NamedModel import BaseNamedModelSerializers
from .Product_count_map import ProductModelSerializers


class CartMOdelSerializers(BaseNamedModelSerializers):

    product_count_map = ProductModelSerializers()
    Users = UsersSerializers(many = True)

    class Meta :
        model = CartModel
        fields = "__all__"