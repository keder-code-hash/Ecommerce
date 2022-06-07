from djongo import models

from .BaseModel import BaseModel

class UserEntity(BaseModel):
    username = models.CharField(max_length=100, unique=True)
    profile_pic_url=models.CharField(null=True,max_length=300,default="https://res.cloudinary.com/dvcjj1k7a/image/upload/v1636390885/Blog/Profile/663328_ti7cnp.png")
    first_name = models.CharField(default='', blank=False, max_length=20)
    last_name = models.CharField(default='', blank=False, max_length=20)
    date_of_birth = models.DateField(null=True, blank=False)
    interests = models.TextField(null=True, max_length=200)
    
    class Meta:
        abstract = True
