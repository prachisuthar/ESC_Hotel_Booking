from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from .forms import *
from django.urls import reverse_lazy
from .forms import DestinationSearchForm
from .models import *
import json


#create views here 




# def savedata(request):
#     json_data = open('destination.json')
#     json_load = json.load(json_data)

#     with open('destination.json','r' ) as data:
#         parsed_json = json.load(data)

#     for result in parsed_json['results']:
#         CountrySearch.objects.create(
#             countryjs = result['term']
#         )


class HomeView(CreateView):
    template_name = "home.html"
    form_class = DestinationSearchForm
    success_url = reverse_lazy("escapp:hotellist")

    def form_valid(self, form):
        
        return super().form_valid(form)

    def savedata(request):
        with open("developer.json", "r") as read_file:
            developer = json.load(read_file)
            for result in developer['results']:
                DestinationSearch.objects.create(
                country = result['term']
            )


class HotelListView(TemplateView):
    template_name = "hotellist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destination_list'] = DestinationSearch.objects.all()

        return context

            

