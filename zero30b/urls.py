from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProviderView.as_view(), name='home'),
    path('about/<int:pk>', AboutProvider.as_view(), name='about_provider'),
    path('create/', CreateProvider.as_view(), name='create_provider'),
    path('shops/', ShopView.as_view(), name='shops')
]