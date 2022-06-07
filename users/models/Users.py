from django.db import models
import uuid 

from .UserEntity import UserEntity

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
 

# from .Address import UsersAddressModel

class UserAddressModel(models.Model):
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,blank=True,default="default")
    description = models.CharField(max_length = 255, blank = True, default=" default description")
    address_line_1 = models.CharField(max_length=300, blank = True)
    address_line_2 = models.CharField(max_length=300, blank = True)
    street_name = models.CharField(max_length=100,blank=True)
    city_name = models.CharField(max_length=50,blank=True)
    state_name = models.CharField(max_length=50,blank=True)
    country_name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    email = models.EmailField(_('email address'),blank=False, max_length=100)
    ph_NO_code = models.CharField(max_length=50)
    ph_NO = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_created=True,auto_now=True)#editable = Flase
    updated_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        abstract = False

##createing a custom user manager for managing the model.
class CustomAccountManager(BaseUserManager):
    def create_user(self, username, password, **other_fields):
        if not username:
            raise ValueError(_('provide an user name')) 
        user = Users(username=username, **other_fields)
        user.set_password(password)
        user.save()
        # print(user)
        return user

    ##creating a super user or a admin for managing the whole things.
    def create_superuser(self,username,password, **other_fields):
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_superuser', True)

        return self.create_user( username,password, **other_fields)
 

class Users(UserEntity,AbstractBaseUser, PermissionsMixin):
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    email = models.EmailField(_('email address'),blank=False, max_length=100)
    ph_NO_code = models.CharField(max_length=50)
    ph_NO = models.CharField(max_length=50)
    
    address = models.ManyToManyField(UserAddressModel,blank=True,verbose_name="user address",related_name="address")


    created_at = models.DateTimeField(auto_created=True,auto_now=True)
    updated_at = models.DateTimeField(auto_created=True,auto_now_add=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['ph_NO']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True
    
    def check_password(self, raw_password: str) -> bool:
        return super().check_password(raw_password)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    class Meta:
        db_table = "Users"




# blacklist token id Autofield changed to BigIntegerField

# class CustomOutStandingToken(OutstandingToken):
#     _id = models.BigIntegerField(primary_key=True, serialize=False,verbose_name="ID")

# class CustomBlackListedToken(BlacklistedToken):
#     _id = models.BigIntegerField(primary_key=True, serialize=False,verbose_name="ID")
    
