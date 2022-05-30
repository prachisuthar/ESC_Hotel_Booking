from dataclasses import fields
from tkinter.ttk import Widget
from django import forms
from .models import *
from .views import * 
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'


class DestinationSearchForm(forms.ModelForm):
    class Meta:
        model = DestinationSearch
        fields = ["country","pax","start_date", "end_date"]
        widgets = {
            'start_date' : DateInput(),
            'end_date' : DateInput()
        }