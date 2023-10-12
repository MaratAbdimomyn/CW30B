from django.db import models

class Provider(models.Model):
    providers_name = models.CharField(max_length=40)
    pace = models.CharField(max_length=40)

class Shop(models.Model):
    shops_name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    my_provider = models.ManyToManyField(Provider, related_name='shops')
