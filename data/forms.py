from attr import fields
from django import forms
from .models import Data
class dataform(forms.ModelForm):
    class Meta:
        model=Data
        fields=["title","content","image","date"]