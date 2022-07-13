from django.db import models
import json
from django.contrib.auth.models import User 
# from .forms import ModelForm 
# Create your models here.


COUNTRY_CHOICES = (
    ('Singapore','Singapore'),
    ('London, UK', 'London, UK'),
    ('Kuala Lumpur, Malaysia','Kuala Lumpur, Malaysia'),
    )

class DestinationSearch(models.Model):
    country = models.CharField(max_length=250, choices = COUNTRY_CHOICES, default = 'Singapore')
    # country = models.CharField(max_length=250)
    # country = models.ForeignKey(CountrySearch, on_delete=models.CASCADE)
    pax = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()


class SingaporeHotelList(models.Model):
    hotel_name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    image = models.ImageField(upload_to = "singapore")
    rating = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

class KLHotelList(models.Model):
    hotel_name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    image = models.ImageField(upload_to = "kl")
    rating = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


class LondonHotelList(models.Model):
    hotel_name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    image = models.ImageField(upload_to = "london")
    rating = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name




