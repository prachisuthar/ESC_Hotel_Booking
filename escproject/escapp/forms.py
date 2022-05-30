from dataclasses import fields
from django import forms
from .models import *
from .views import * 


class DestinationSearchForm(forms.ModelForm):
    class Meta:
        model = DestinationSearch
        fields = ["country","pax",]