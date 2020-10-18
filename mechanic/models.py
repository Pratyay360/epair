from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _






class Message1(models.Model):
    phoneno=models.BigIntegerField(null=True)
    message=models.TextField(max_length=200,default=0)
