import email
from statistics import mode
from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=200, blank=True)
    phone = models.BigIntegerField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name 
        

