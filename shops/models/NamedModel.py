from django.db import models
import uuid
from users.models.BaseModel import BaseModel

class BaseNamedmodel(BaseModel):
    name = models.CharField(max_length=255,blank=True,default="default")
    description = models.CharField(max_length = 255, blank = True, default=" default description")
    created_at = models.DateTimeField(auto_created=True,auto_now=True)#editable = Flase
    updated_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    class Meta : 
        abstract = True

class NamedModel(BaseModel): 
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,blank=True,default="default")
    description = models.CharField(max_length = 255, blank = True, default=" default description")
    created_at = models.DateTimeField(auto_created=True,auto_now=True)#editable = Flase
    updated_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    class Meta : 
        abstract = True