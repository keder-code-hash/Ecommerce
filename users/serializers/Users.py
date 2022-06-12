from .UserEntity import UserEntitySerializers
from ..models.Users import Users,UserAddressModel 
from .Address import AddressSerializers

class UsersSerializers(UserEntitySerializers):
    address = AddressSerializers(many = True)
    delivery_address = AddressSerializers(many = True)

    class Meta:
        model = Users
        fields = "__all__"   
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self,validated_data):
        user_address = validated_data.pop('address')
        user_delivery_address = validated_data.pop('delivery_address')
        customUser=Users.objects.create_user(validated_data['email'] ,validated_data['username']
                    ,validated_data['password'])
        
        for user_add in user_address:
            user_address_obj = UserAddressModel.objects.create(**user_add)
            user_address_obj.save()
            customUser.address.add(user_address_obj)

        for user_add in user_delivery_address:
            user_address_obj = UserAddressModel.objects.create(**user_add)
            user_address_obj.save()
            customUser.delivery_address.add(user_address_obj)
        
        return customUser
    

    def update(self, instance, validated_data):
        user_address = validated_data.pop('address')
        user_delivery_address = validated_data.pop('delivery_address')

        user_adderss_inst= list((instance.address).all())
        user_delivery_address_inst= list((instance.delivery_address).all())

        # assert(instance)

        user_adderss_list= list(user_adderss_inst)
        user_delivery_address_list= list(user_delivery_address_inst)

        instance.username = validated_data.get('username',instance.username)
        instance.profile_pic_url = validated_data.get('profile_pic_url',instance.profile_pic_url)
        instance.first_name = validated_data.get('first_name',instance.first_name) 
        instance.last_name = validated_data.get('last_name',instance.last_name) 
        instance.date_of_birth = validated_data.get('date_of_birth',instance.date_of_birth) 
        instance.interests = validated_data.get('interests',instance.interests) 
        instance.identifier = validated_data.get('identifier',instance.identifier) 
        instance.is_active = validated_data.get('is_active',instance.is_active) 
        instance.is_staff = validated_data.get('is_staff',instance.is_staff) 
        instance.is_admin = validated_data.get('is_admin',instance.is_admin) 
        instance.is_superuser = validated_data.get('is_superuser',instance.is_superuser) 
        instance.is_verified = validated_data.get('is_verified',instance.is_verified) 
        instance.email  = validated_data.get('email',instance.email)
        instance.ph_NO_code = validated_data.get('ph_NO_code',instance.ph_NO_code) 
        instance.ph_NO  = validated_data.get('ph_NO',instance.ph_NO)
        instance.gender = validated_data.get('gender',instance.gender) 

        instance.save()

        for user_add in user_address:
            user_addr = user_adderss_list.pop(0)

            user_addr.identifier = user_add.get('identifier',user_addr.identifier) 
            user_addr.name = user_add.get('name',user_addr.name) 
            user_addr.description = user_add.get('description',user_addr.description) 
            user_addr.address_line_1 = user_add.get('address_line_1',user_addr.address_line_1) 
            user_addr.address_line_2 = user_add.get('address_line_2',user_addr.address_line_2) 
            user_addr.street_name = user_add.get('street_name',user_addr.street_name) 
            user_addr.city_name = user_add.get('city_name',user_addr.city_name) 
            user_addr.state_name = user_add.get('state_name',user_addr.state_name) 
            user_addr.country_name = user_add.get('country_name',user_addr.country_name) 
            user_addr.zip_code = user_add.get('zip_code',user_addr.zip_code) 
            user_addr.email = user_add.get('email',user_addr.email) 
            user_addr.ph_NO_code = user_add.get('ph_NO_code',user_addr.ph_NO_code) 
            user_addr.ph_NO = user_add.get('ph_NO',user_addr.ph_NO) 

            user_addr.save()

        for user_add in user_delivery_address:
            user_addr = user_delivery_address_list.pop(0)

            user_addr.identifier = user_add.get('identifier',user_addr.identifier) 
            user_addr.name = user_add.get('name',user_addr.name) 
            user_addr.description = user_add.get('description',user_addr.description) 
            user_addr.address_line_1 = user_add.get('address_line_1',user_addr.address_line_1) 
            user_addr.address_line_2 = user_add.get('address_line_2',user_addr.address_line_2) 
            user_addr.street_name = user_add.get('street_name',user_addr.street_name) 
            user_addr.city_name = user_add.get('city_name',user_addr.city_name) 
            user_addr.state_name = user_add.get('state_name',user_addr.state_name) 
            user_addr.country_name = user_add.get('country_name',user_addr.country_name) 
            user_addr.zip_code = user_add.get('zip_code',user_addr.zip_code) 
            user_addr.email = user_add.get('email',user_addr.email) 
            user_addr.ph_NO_code = user_add.get('ph_NO_code',user_addr.ph_NO_code) 
            user_addr.ph_NO = user_add.get('ph_NO',user_addr.ph_NO) 

            user_addr.save()

        return instance


