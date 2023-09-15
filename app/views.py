from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import One
from django.urls import reverse, reverse_lazy
from .forms import *