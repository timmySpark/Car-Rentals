from django.db import models

# Create your models here.

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


class ContactInfo(models.Model):
    detail_icon = models.CharField(max_length=200)
    detail_subject = models.CharField(max_length=200)
    details = models.CharField(max_length=300)
    

    class Meta:
        verbose_name = ("Contact Info")
        verbose_name_plural = ("Contact Information")

    def __str__(self):
        return f'{self.detail_subject} ------------- {self.details}'

    


