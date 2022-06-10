from .UserEntity import UserEntitySerializers
from ..models.Users import Users 
from .Address import AddressSerializers

class UsersSerializers(UserEntitySerializers):
    address = AddressSerializers(many = True)
    delivery_address = AddressSerializers(many = True)
    class Meta:
        model = Users
        fields = "__all__"   
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self,validated_data):
        customUser=Users.objects.create_user(validated_data['username']
                    ,validated_data['password'])
        return customUser