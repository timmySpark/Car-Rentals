from django.shortcuts import render , redirect , get_object_or_404
from app.forms import * 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
        'link':'home'
    }
    return render(request, template_name,context)

def about_view(request):
    template_name='about.html'
    context={
        'link':'about'
    }
    return render(request, template_name,context)


@login_required(login_url='acct/login')
def cars_view(request):
    template_name='cars.html'
    cars = Cars.objects.all()
    context={
        'cars':cars,
        'link':'cars'
    }
    return render(request, template_name,context)

def car_type_view(request,slug):
    template_name='cars.html'
    getcars = get_object_or_404(CarType,slug=slug)
    car = Cars.objects.filter(getcars__slug=slug)
    page = request.GET.get('page',1)
    paginator= Paginator(car, 3)

    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    context={
        'getcars':getcars,
        'car_types':cars,
    }
    return render(request, template_name,context)


@login_required(login_url='acct/login')
def car_details_view(request,slug):
    template_name='car-details.html'
    details = get_object_or_404(Cars,slug=slug)
    # main_specs = MainSpecs.objects.all()
    context={
        'details':details,     
        'link':'cars'
        # 'main_specs':main_specs, 
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
        'link':'book'
    }
    return render(request, template_name,context)    

 
def services_view(request):
    template_name='services.html'
    car_type = CarType.objects.all()
    car_brands = Brands.objects.all()
    context={
        'cartypes':car_type,
        'carbrands': car_brands,
        'link':'services'
    }
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

def subscriber_view(request):
    template_name='index.html'
    form = SubscriberForm()
    if request.POST:
        form = SubscriberForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Invalid Submission ,Request failed')
    context={
        'Subscribers_form':form,
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
        'link':'contact'
        }
    return render(request, template_name,context)           


def not_found_view(request):
    template_name='404.html'
    return render(request, template_name)

