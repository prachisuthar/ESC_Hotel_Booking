from django.db import models
# from .forms import ModelForm 
# Create your models here.


COUNTRY_CHOICES = (
    ('Singapore','Singapore'),
    ('London', 'London'),
    ('Malaysia','Malaysia'),
    )

class DestinationSearch(models.Model):
    country = models.CharField(max_length=250, choices = COUNTRY_CHOICES, default = 'Singapore')
    pax = models.IntegerField()


    def __str__(self):
        return self.country()

