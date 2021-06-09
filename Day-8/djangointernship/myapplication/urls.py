from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview,name="Home"),
    path('about',views.aboutpageview,name="About"),
    path('register',views.registerpageview,name="Register")
]