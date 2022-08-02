from attr import fields
from django import forms
from .models import Article
class aricleform(forms.ModelForm):
    class Meta:
        model=Article
        fields=["title","content","image","date"]