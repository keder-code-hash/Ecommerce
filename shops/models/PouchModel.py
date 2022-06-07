from django.db import models
from .NamedModel import NamedModel
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
 
 
def validate_amount(value):
    if value <= 0 :
        raise ValidationError(
            _('%(value)s is not an proper amount.Check it out.'),
            params={'value': value},
        )

AMOUNT_UNIT_CHOICES = [
    ('KG', 'KiloGram'),
    ('GR', 'Gram'),
    ('LT', 'Litre'),
    ('KL', 'KiloLitre')
]

class PouchModel(NamedModel):
    amount = models.IntegerField(unique=True,validators=[validate_amount])
    unit =   models.CharField(
                    max_length=2,
                    choices=AMOUNT_UNIT_CHOICES,
                    default='GR',
             )
    class Meta:
        abstract = False
