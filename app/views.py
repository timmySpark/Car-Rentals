from django.shortcuts import render , redirect
from app.forms import * 
from django.contrib.auth.decorators import login_required
from django.contrib import messages 


# Create your views here.

def home_view(request):
    template_name='index.html'
    testimonials = Testimonial.objects.all() # move to context_processor.py
    form = BookingForm()
    if request.POST:
        form = BookingForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Invalid Submission ,Request failed')
    context={
        'bookingform':form,
        'testimonials':testimonials,
    }
    return render(request, template_name,context)

def about_view(request):
    template_name='about.html'
    testimonials = Testimonial.objects.all()
    context={
        'testimonials':testimonials,
    }
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
    contact_info = ContactInfo.objects.all()
    form = ContactForm()
    if request.POST:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            messages.error(request, 'Invalid Submission , failed')

    context={
        'contact':form,
        'contact_info':contact_info
        }
    return render(request, template_name,context)           


