from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    about = models.TextField()
    org = models.CharField(max_length=200)
    date = models.DateField()
    img_url = models.URLField(max_length=500, blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    
class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    mobile_no = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit mobile number.')
        ]
    )
    address = models.TextField()
    registered_at = models.DateTimeField(auto_now_add=True)