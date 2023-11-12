from django import forms
from .models import Appointment

class SubscribeForm(forms.Form):
        email = forms.EmailField(label = "Email",max_length=50, widget=forms.EmailInput(attrs={'placeholder' : 'Enter your email'}))
        
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['Name', 'Number','form_email','form_date','choose_schedule']
        