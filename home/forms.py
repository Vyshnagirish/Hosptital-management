from django import forms
from .models import *

class DepForm(forms.ModelForm):
    class Meta:
        model = Department
        fields="__all__"

        widgets={
        'dep_name':forms.TextInput(attrs={
            'placeholder':"Enter department name"
        })
        }

class DocForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets={
            'appointment_date' : forms.DateInput(attrs={
                'type':"date"
            })
        }
        