from django.contrib import admin
from .models import Message

# Register your models here.
from services.models import services
admin.site.register(services)
admin.site.register(Message)