from djongo import models
from django.utils.translation import gettext_lazy as _
from .BaseModel import BaseModel

class Contact(BaseModel):
    email = models.EmailField(_('email address'),blank=False, max_length=100)
    ph_NO_code = models.CharField(max_length=50)
    ph_NO = models.CharField(max_length=50)
    class Meta:
        abstract = True