from django.shortcuts import render
from app.forms import forms 
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_view(request):
    template_name='index.html'
    context={}
    return render(request, template_name,context)

def about_view(request):
    template_name='about.html'
    context={}
    return render(request, template_name,context)


@login_required(login_url='acct/login')
def cars_view(request):
    template_name='cars.html'
    context={}
    return render(request, template_name,context)

@login_required(login_url='acct/login')
def car_details_view(request):
    template_name='car-details.html'
    context={}
    return render(request, template_name,context)

    
@login_required(login_url='acct/login')
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
    form = ContactForm()
    if request.POST:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
    context={}
    return render(request, template_name,context)           


