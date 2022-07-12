from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView, View
from .forms import *
from django.urls import reverse_lazy
from .forms import DestinationSearchForm, SignUpForm, LoginForm
from .models import *
import json
from django.contrib.auth import authenticate, login, logout



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
        # context['country_list'] = DestinationSearch.country.

        context['singapore_list'] = SingaporeHotelList.objects.all()

        return context

            
class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("escapp:home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)
       
        return super().form_valid(form) #and render(request,"sendemail.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('escapp:home')

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy("escapp:home")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        
        if usr is not None and usr.customer:
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid Credentials"})

        return super().form_valid(form)