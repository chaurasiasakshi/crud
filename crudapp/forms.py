from django import forms

from .models import *


class crudForm(forms.ModelForm):
    class Meta:
        model = crud
        fields= '__all__'