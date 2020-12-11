from django import forms
from .models import Gallery


class HotelForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image', 'category']