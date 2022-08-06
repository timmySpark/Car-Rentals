from .models import *
from random import sample


def fast_cars_renderer(request):
    about = About.objects.all()
    banner = Banner.objects.all()
    car_brands = Brands.objects.all()
    cars = Cars.objects.all()
    counter = 2
    random_cars = sample(list(cars),counter)
    features = Features.objects.all()
    contact_info = ContactInfo.objects.all()
    # experience = Experience.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    


    return{
        'about_us':about,
        'banner':banner,
        'related_cars':random_cars,
        'car_brands':car_brands,
        'contact_info':contact_info,
        # 'experience':experience,
        'services':services,
        'testimonials':testimonials,

    }