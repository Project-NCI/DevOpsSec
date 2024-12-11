from django import forms
from .models import Event, EventRegistration

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['mobile_no', 'address']
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
        
class AdminAddForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'about', 'org', 'date', 'img_url']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of the event'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'About',
                'rows': 4
            }),
            'org': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Organizer',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'img_url': forms.URLInput(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'name': 'Name of the Event:',
            'location': 'Location:',
            'about': 'About the event:',
            'org': 'Name of the Organizer:',
            'date': 'Enter Date:',
            'img_url': 'Enter URL of the image in s3'
        }

class AdminEditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'about', 'org', 'date']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
            }),
            'org': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial', {})
        super().__init__(*args, **kwargs)

        self.fields['name'].initial = initial.get('name', self.instance.name if self.instance else '')
        self.fields['location'].initial = initial.get('location', self.instance.location if self.instance else '')
        self.fields['about'].initial = initial.get('about', self.instance.about if self.instance else '')
        self.fields['org'].initial = initial.get('org', self.instance.org if self.instance else '')
        self.fields['date'].initial = initial.get('date', self.instance.date if self.instance else '')