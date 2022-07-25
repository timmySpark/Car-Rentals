from django.shortcuts import render

# Create your views here.

def home_view(request):
    template_name='index.html'
    context={}
    return render(request, template_name,context)

def about_view(request):
    template_name='about.html'
    context={}
    return render(request, template_name,context)

def cars_view(request):
    template_name='cars.html'
    context={}
    return render(request, template_name,context)

def car_details_view(request):
    template_name='car-details.html'
    context={}
    return render(request, template_name,context)

def pricing_view(request):
    template_name= 'pricing.html'
    context={}
    return render(request, template_name,context)

def services_view(request):
    template_name='services.html'
    context={}
    return render(request, template_name,context)           

def contact_view(request):
    template_name='contact.html'
    context={}
    return render(request, template_name,context)           


