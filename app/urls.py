from django.urls import path 
from app.views import *


urlpatterns = [
     path('', home_view,name='home'),
     path('about',about_view,name='about'),
     path('cars',cars_view,name='cars'),
     path('car-details',car_details_view,name='car_details'),
     path('pricing',pricing_view,name='pricing'),
     path('services',services_view,name='services'),
     path('contact',contact_view,name='contact'),
]