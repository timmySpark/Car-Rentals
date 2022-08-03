from .models import *

def fast_cars_renderer(request):
    about = About.objects.all()
    banner = Banner.objects.all()
    car_brands = Brands.objects.all()
    contact_info = ContactInfo.objects.all()
    # experience = Experience.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()

    return{
        'about_us':about,
        'banner':banner,
        'car_brands':car_brands,
        'contact_info':contact_info,
        # 'experience':experience,
        'services':services,
        'testimonials':testimonials,

    }