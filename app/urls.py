from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

 
urlpatterns = [
     path('', home_view,name='home'),
     path('about',about_view,name='about'),
     path('cars',cars_view,name='cars'),
     path('cars/<str:slug>',car_type_view,name='car-services' ),
     path('car-details/<str:slug>',car_details_view,name='car-details'),
     path('pricing',pricing_view,name='pricing'),
     path('book',booking_view,name='book'),
     path('services',services_view,name='services'),
     path('post-testimonials',post_testimonials_view,name='post-testimonials'),
     path('contact',contact_view,name='contact'),
     path('404',not_found_view,name='404'),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)