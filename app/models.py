from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class About(models.Model):
    image = models.ImageField(upload_to='AboutImages')  
    title = models.CharField(max_length=150)
    text  = models.TextField()
    years_experienced = models.IntegerField()
    total_cars = models.IntegerField()
    happy_customers = models.IntegerField()
    total_branches = models.IntegerField()

    class Meta:
        verbose_name = ("About Us")
        verbose_name_plural = ("About Fast Cars")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("About_detail", kwargs={"pk": self.pk})


class Book(models.Model):
    pick_up_location = models.CharField(max_length=300)
    drop_off_location = models.CharField(max_length=300)
    pick_up_date = models.CharField(max_length=50 ,blank=False)
    drop_off_date = models.CharField(max_length=50 ,blank=False)
    pick_up_time = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = ("Booking Detail")
        verbose_name_plural = ("Booking Details")

    def __str__(self):
        return f'---From---{self.pick_up_location} ---To---- {self.drop_off_location}'

    def get_absolute_url(self):
        return reverse("Booking_detail", kwargs={"pk": self.pk})


class Brands(models.Model):
    car_brand = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    

    class Meta:
        verbose_name = ("Car Brand")
        verbose_name_plural = ("Car Brands")

    def __str__(self):
        return self.car_brand


    def save(self, *args, **kwargs):
        slug = self.name
        if not self.slug:
            self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):   
        return reverse("category_detail", kwargs={"pk": self.pk}) 


class Cars(models.Model):
    car_model = models.CharField(max_length=200)
    car_name=models.CharField(max_length=300)
    image =models.ImageField(upload_to='CarImages/')
    price = models.IntegerField()
    # category= models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=500, unique=True, blank=True)

    class Meta:
        verbose_name = ("Car")
        verbose_name_plural = ("Cars")

    def __str__(self):
        return f'{self.car_model} ----------- {self.car_name}'

    def save(self, *args, **kwargs):
        slug = self.car_name
        if not self.slug:
            self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)     

    def get_absolute_url(self):
        return reverse("Car_detail", kwargs={"pk": self.pk})


class ContactDetail(models.Model):
    name = models.CharField(max_length=100,help_text='John Doe')
    email = models.EmailField(max_length=254,help_text="JD@gmail.com")
    subject = models.CharField(max_length=100,help_text="Greetings")
    message = models.TextField(help_text='Hello There')
    

    class Meta:
        verbose_name = ("Contact Detail")
        verbose_name_plural = ("Contact Details")

    def __str__(self):
        return f'{self.name} ------------- {self.email}'

    def get_absolute_url(self):
        return reverse("Contactdetails", kwargs={"pk": self.pk})    


class ContactInfo(models.Model):
    detail_icon = models.CharField(max_length=200)
    detail_subject = models.CharField(max_length=200)
    details = models.CharField(max_length=300)
    

    class Meta:
        verbose_name = ("Contact Info")
        verbose_name_plural = ("Contact Information")

    def __str__(self):
        return f'{self.detail_subject} ------------- {self.details}'

    def get_absolute_url(self):
        return reverse("ContactInfo_details", kwargs={"pk": self.pk})    

    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image =models.ImageField(upload_to='TestimonialImages/')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Testimonial")
        verbose_name_plural = ("Testimonials")

    def __str__(self):
        return f'{self.name} ----------- {self.profession}'

    def get_absolute_url(self):
        return reverse("Testimonial_detail", kwargs={"pk": self.pk})


