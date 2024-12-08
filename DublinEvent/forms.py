from django import forms
from .models import Event, EventRegistration

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['mobile_no', 'address']  # Include only the mobile number and address fields
        widgets = {
            'mobile_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your 10-digit mobile number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address',
                'rows': 4
            }),
        }
        labels = {
            'mobile_no': 'Mobile Number',
            'address': 'Address',
        }
