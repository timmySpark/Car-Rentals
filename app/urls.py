from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from app.views import *


urlpatterns = [
     path('', home_view,name='home'),
     path('about',about_view,name='about'),
     path('cars',cars_view,name='cars'),
     path('car-details',car_details_view,name='car_details'),
     path('pricing',pricing_view,name='pricing'),
     path('book',booking_view,name='book'),
     path('services',services_view,name='services'),
     path('contact',contact_view,name='contact'),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)