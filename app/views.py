from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import *

class ProviderView(ListView):
    model = Provider
    template_name = 'home.html'
    context_object_name = 'providers'

class AboutProvider(DetailView):
    model = Provider
    template_name = 'about_provider.html'
    context_object_name = 'provider'

class CreateProvider(CreateView):
    model = Provider
    form_class = ProviderForm
    template_name = 'create_provider.html'
    success_url = reverse_lazy('home')

class ShopView(ListView):
    model = Shop
    template_name = 'shops.html'
    context_object_name = 'shops'