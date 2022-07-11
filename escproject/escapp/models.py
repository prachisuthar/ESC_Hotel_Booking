from django.db import models
import json
# from .forms import ModelForm 
# Create your models here.


# COUNTRY_CHOICES = (
#     ('Singapore','Singapore'),
#     ('London', 'London'),
#     ('Malaysia','Malaysia'),
#     )

class DestinationSearch(models.Model):
    # country = models.CharField(max_length=250, choices = COUNTRY_CHOICES, default = 'Singapore')
    country = models.CharField(max_length=250)
    # country = models.ForeignKey(CountrySearch, on_delete=models.CASCADE)
    pax = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()


class CountrySearch(models.Model):
    countryjs = models.CharField(max_length=250)


