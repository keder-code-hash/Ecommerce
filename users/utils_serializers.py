# from Authentication import settings
from .models.Users import Users
from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth import password_validation 
from django.utils.translation import gettext_lazy as _

from .serializers.Users import UsersSerializers
# class UserSerializers(serializers.ModelSerializer):
#     class Meta :
#         model = Register
#         fields = "__all__"

 
class LoginSerializer(serializers.Serializer): 
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    ph_NO = serializers.CharField(max_length = 255, read_only = True)
    email = serializers.CharField(max_length = 255, read_only = True)
    user = UsersSerializers(read_only = True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = Users.objects.get(username__iexact=obj['username'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        } 
 

    def validate(self,attrs):
        username = attrs.get('username', 'Keder')
        password = attrs.get('password', '')
        filtered_user_by_username = Users.objects.filter(username=username)
        # print(filtered_user_by_username)
        # user = auth.authenticate(username=username, password=password)

        user = None
        if Users.objects.get(username__iexact = username).check_password(password):
            user = Users.objects.get(username__iexact = username)

        if filtered_user_by_username.exists() == False:
            raise AuthenticationFailed(
                detail='Invalid user name. Please check it out.')

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        # if not user.is_verified:
        #     raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'username': user.username,
            'first_name' : user.first_name,
            'tokens': user.tokens ,
            'ph_NO' : user.ph_NO,
            'user':user
        }

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    } 


class ResetPasswordEmailSentSerializers(serializers.Serializer):
    email = serializers.EmailField()
    class Meta:
        field = ['email']


class ResetPasswordSerializers(serializers.Serializer):
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
        "password_requirements" : _("Password did not match with minimum password validation Requirements")
    }
    new_password1 = serializers.CharField(max_length = 200 )
    new_password2 = serializers.CharField(max_length = 200 )
 
    def validate(self, attrs):
        try:
            password_validation.validate_password(attrs.get("new_password1"))
            if attrs.get("new_password1") and attrs.get("new_password2") : 
                if attrs.get("new_password1") != attrs.get("new_password2"):
                    raise serializers.ValidationError(self.error_messages.get("password_mismatch"))
            return attrs  
        except:
            raise serializers.ValidationError(self.error_messages.get("password_requirements"))
        

    def save(self,user):
        password = self.validated_data.get("new_password1")
        user.set_password(password)
        user.save()
        return user