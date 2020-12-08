from django.contrib import admin
from .models import CustomUser, MechanicProfile
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(MechanicProfile)
