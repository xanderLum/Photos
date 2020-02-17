from django import forms
from .models import Photo


class PhotoForm(forms.Form):
    caption = forms.CharField(max_length=500)
    file = forms.ImageField()
