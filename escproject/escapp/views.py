from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from .forms import *
from django.urls import reverse_lazy
from .forms import DestinationSearchForm
from .models import *


#create views here 
class HomeView(CreateView):
    template_name = "home.html"
    form_class = DestinationSearchForm
    success_url = reverse_lazy("escapp:home")

    def form_valid(self, form):
        
        return super().form_valid(form)



