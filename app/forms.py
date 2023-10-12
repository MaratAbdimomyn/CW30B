from django import forms
from django.forms import ModelForm
from .models import *

class ShopForm(forms.ModelForm):
    
    class Meta:
        model = Shop
        fields = ('shops_name', 'location', 'my_provider')

class ProviderForm(forms.ModelForm):
    
    class Meta:
        model = Provider
        fields = ('providers_name', 'pace')
