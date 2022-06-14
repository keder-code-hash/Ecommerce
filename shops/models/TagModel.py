from .NamedModel import NamedModel
from django.db import models

class Tagmodel(NamedModel):
    tag_img = models.ImageField(upload_to = 'tag_image/')
    class Meta :
        abstract = False
    
    def __str__(self) -> str:
        return self.name