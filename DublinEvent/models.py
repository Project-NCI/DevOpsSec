from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    about = models.TextField()
    org = models.CharField(max_length=200)
    date = models.DateField()
    img_url = models.URLField(max_length=500, blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)