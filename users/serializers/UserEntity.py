from .BaseModel import BaseModelSerializers
from rest_framework import serializers

class UserEntitySerializers(BaseModelSerializers):
    username = serializers.CharField(max_length=100)
    profile_pic_url=serializers.CharField(max_length = 300)
    first_name = serializers.CharField( max_length=20)
    last_name = serializers.CharField(max_length=20)
    date_of_birth = serializers.DateField()
    interests = serializers.CharField(max_length=200)
     
