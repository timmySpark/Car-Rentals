from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# from multiselectfield import MultiSelectField

# Create your models here.

class About(models.Model):
    image = models.ImageField(upload_to='AboutImages/')  
    title = models.CharField(max_length=150)
    text  = models.TextField()


    class Meta:
        verbose_name = ("About Us")
        verbose_name_plural = ("About Fast Cars")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("About_detail", kwargs={"pk": self.pk})


class Banner(models.Model):
    banner_img = models.ImageField(upload_to='BannerImg/')
    text = models.CharField(max_length = 300)
    btn_text = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("Banner")
        verbose_name_plural =("Banners")

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("Banner_details", kwargs={"pk": self.pk})


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
    brand_image = models.ImageField(upload_to="BrandImages/")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    

    class Meta:
        verbose_name = ("Car Brand")
        verbose_name_plural = ("Car Brands")

    def __str__(self):
        return self.car_brand


    def save(self, *args, **kwargs):
        slug = self.car_brand
        if not self.slug:
            self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):   
        return reverse("category_detail", kwargs={"pk": self.pk}) 


class Features(models.Model):
    features = models.CharField(max_length=500)
    

    class Meta:
        verbose_name = ("Feature")
        verbose_name_plural = ("Features")

    def __str__(self):
        return self.features



class MainSpecs(models.Model):
    icon = models.CharField(max_length=20)
    spec = models.CharField(max_length=500)
    spec_value = models.CharField(max_length=400)
    

    class Meta:
        verbose_name = ("Main Spec")
        verbose_name_plural = ("Main Specs")

    def __str__(self):
        return self.spec


class Cars(models.Model):
    car_make = models.ForeignKey(Brands,on_delete=models.CASCADE)
    car_model = models.CharField(max_length=200)
    image =models.ImageField(upload_to='CarImages/')
    description = models.TextField()
    features =models.ManyToManyField(Features)
    year = models.IntegerField()
    price = models.IntegerField()
    slug = models.SlugField(max_length=500, unique=True, blank=True)

    class Meta:
        verbose_name = ("Car")
        verbose_name_plural = ("Car Details")

    def __str__(self):
        return f'{self.car_make} -----------  {self.car_model}  '

    def save(self, *args, **kwargs):
        slug = self.car_model
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


'''   
class Experience(models.Model):
    years_experienced = models.IntegerField()
    total_cars = models.IntegerField()
    happy_customers = models.IntegerField()
    total_branches = models.IntegerField()
    

    class Meta:
        verbose_name = ("Experience")
        verbose_name_plural = ("Our Experiences")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Experience_detail", kwargs={"pk": self.pk})
'''

class Service(models.Model):
    icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=100)
    service_text = models.CharField(max_length=400)
    

    class Meta:
        verbose_name =("Service")
        verbose_name_plural =("Services")

    def __str__(self):
        return self.service_title

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})


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


