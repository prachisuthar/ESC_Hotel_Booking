from django.db import models
import json
from django.contrib.auth.models import User 
# from .forms import ModelForm 
# Create your models here.


class DestinationSearch(models.Model):
    country = models.CharField(max_length=250)
    pax = models.PositiveIntegerField()
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

# json_file_path = "trial.json"

# with open(json_file_path, 'r', encoding="utf8") as j:
#     searchResults = json.loads(j.read())

# for searchResult in searchResults['results']: 
#     DestinationSearch.objects.create(country = searchResult['term'], pax=searchResult['lng'], start_date = "2000-10-11", end_date = "2000-11-12")

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
    full_name = models.CharField(max_length=250)

    def __str__(self):
        return self.full_name

class Booking(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    request = models.CharField(max_length=5000)
    credit_card_no = models.PositiveIntegerField()
    expiry = models.PositiveBigIntegerField()
    cvv = models.PositiveIntegerField()
    billing_address = models.CharField(max_length=500)






