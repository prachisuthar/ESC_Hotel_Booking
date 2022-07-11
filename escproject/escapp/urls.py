from django.urls import path 
from .views import * 

app_name = "escapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("/hotelist", HotelListView.as_view(), name="hotellist"),
   
]