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

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")

