from .models import *

def fast_cars_renderer(request):
    about = About.objects.all()
    contact_info = ContactInfo.objects.all()
    # experience = Experience.objects.all()
    testimonials = Testimonial.objects.all()

    return{
        'about_us':about,
        'contact_info':contact_info,
        # 'experience':experience,
        'testimonials':testimonials,

    }