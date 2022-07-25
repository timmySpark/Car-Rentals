from django.urls import path 
from app.views import *


urlpatterns = [
     path('', home_view,name='home'),
     path('about',about_view,name='about'),
     path('cars',cars_view,name='cars'),
     path('contact',contact_view,name='contact'),
]