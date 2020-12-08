from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


#User Create From Signup
class CustomUser(AbstractUser):
    username = None
    first_name=models.CharField(max_length=25,null=True)
    last_name=models.CharField(max_length=25,null=True)
    phoneno=models.BigIntegerField(null=True)
    email = models.EmailField(_('email address'),unique=True)
    userflag = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name','first_name','phoneno']
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

#Mechanic Profile From Mechanic  
class MechanicProfile(models.Model):
    user = models.ForeignKey(CustomUser,related_name='mechanocs',on_delete=models.CASCADE)
    postalcode = models.BigIntegerField(null=True)
    address = models.TextField(default='',null=True)
    category = models.CharField(max_length=25,null=True)
    phoneno = models.BigIntegerField(null=True)
    email = models.EmailField(_('email address'),unique=True)

    def __str__(self):
        return (self.category) 
