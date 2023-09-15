from django import forms
from django.forms import ModelForm
from .models import *

class Form(forms.ModelForm):
    
    class Meta:
        model = Shop
        fields = ('shops_name', 'location')

class Provider(forms.ModelForm):
    
    class Meta:
        model = Provider
        fields = ('providers_name', 'pace')