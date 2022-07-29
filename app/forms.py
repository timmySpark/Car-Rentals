from django import forms
from app.models import*


class BookingForm(forms.ModelForm):
    class Meta:
        model = Book 
        exclude = ['created_at']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields='__all__'