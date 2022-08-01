from django.shortcuts import render , redirect , get_object_or_404
from app.forms import * 
from django.contrib.auth.decorators import login_required
from django.contrib import messages 


# Create your views here.

def home_view(request):
    template_name='index.html'
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
    }
    return render(request, template_name,context)

def about_view(request):
    template_name='about.html'
    context={
    }
    return render(request, template_name,context)


@login_required(login_url='acct/login')
def cars_view(request):
    template_name='cars.html'
    cars = Cars.objects.all()
    context={
        'cars':cars,
    }
    return render(request, template_name,context)

@login_required(login_url='acct/login')
def car_details_view(request,slug):
    template_name='car-details.html'
    details = get_object_or_404(Cars,slug=slug)
    context={
        'details':details,      
    }
    return render(request, template_name,context)

    
@login_required(login_url='acct/login')
def pricing_view(request):
    template_name= 'pricing.html'
    context={}
    return render(request, template_name,context)


@login_required(login_url='acct/login')
def booking_view(request):
    template_name= 'book.html'
    form = BookingForm()
    if request.POST:
        form = BookingForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('book')
        else:
            messages.error(request, 'Invalid Submission ,Request failed')
    context={
        'bookingform':form,
    }
    return render(request, template_name,context)    

 
def services_view(request):
    template_name='services.html'
    context={}
    return render(request, template_name,context)           

@login_required(login_url='acct/login')
def post_testimonials_view(request):
    template_name='post-testimonials.html'
    form = TestimonialForm()
    if request.POST:
        form = TestimonialForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            messages.error(request, 'Invalid Submission ,Request failed')
    context={
        'post_testimonials':form,
    }
    return render(request, template_name,context)


def contact_view(request):
    template_name='contact.html'
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
        }
    return render(request, template_name,context)           


