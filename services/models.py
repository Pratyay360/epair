from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class services(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    desc = models.TextField()
    date = models.DateField()
    catagory = models.CharField(max_length=50, null=True)
    Status_Closed = models.BooleanField(default=False)
    def __str__(self):
        return self.pincode
    
