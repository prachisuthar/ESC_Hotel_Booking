from django.urls import path 
from .views import * 

app_name = "escapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("hotellist/", HotelListView.as_view(), name="hotellist"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(), name="login"),
    path("booking/", BookingView.as_view(), name="booking"),

]