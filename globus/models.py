from .models import *
from django.db import models
from django.utils import timezone



class Product(models.Model):

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    price = models.FloatField()



class User(models.Model):

    user = models.CharField(max_length=50)
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
