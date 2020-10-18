from django.contrib import admin
from .models import CustomUser, MechanicProfile, OTP,OtpDirectory
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(MechanicProfile)
admin.site.register(OTP)
admin.site.register(OtpDirectory)