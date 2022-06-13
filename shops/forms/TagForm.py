from ..models.TagModel import Tagmodel
from django import forms

class TagChangeListForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tagmodel.objects.all(),required = False)
     