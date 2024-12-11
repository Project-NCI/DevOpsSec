from django import forms
from .models import Event, EventRegistration

class EventRegistrationForm(forms.ModelForm):
    """
    Form to register for an event.
    """
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
    """
    Form to add a new event.
    """
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
                'placeholder': 'About the event',
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
            'name': 'Name of the Event',
            'location': 'Location',
            'about': 'About the Event',
            'org': 'Name of the Organizer',
            'date': 'Event Date',
            'img_url': 'Image URL (S3)',
        }

class AdminEditForm(forms.ModelForm):
    """
    Form to edit an existing event.
    """
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
        """
        Custom initial values.
        """
        initial = kwargs.pop('initial', {})
        super().__init__(*args, **kwargs)

        # Set initial values based on existing (pre)
        if self.instance:
            self.fields['name'].initial = initial.get('name', self.instance.name)
            self.fields['location'].initial = initial.get('location', self.instance.location)
            self.fields['about'].initial = initial.get('about', self.instance.about)
            self.fields['org'].initial = initial.get('org', self.instance.org)
            self.fields['date'].initial = initial.get('date', self.instance.date)
