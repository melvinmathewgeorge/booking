from django import forms
from .models import Package, Booking

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'overview', 'cost']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['package', 'customer_name', 'customer_email', 'booking_date', 'number_of_people', 'status']
