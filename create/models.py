import email
from django.db import models

# Create your models here.

class contacts(models.Model):
    name=models.CharField(max_length=50,default=None)
    phone_number=models.CharField(max_length=20,default=None)
    email=models.EmailField(max_length=100,default=None)