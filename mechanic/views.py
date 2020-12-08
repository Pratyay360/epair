from datetime import datetime
from login.models import CustomUser, MechanicProfile
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponse, request
import random
import requests
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache




# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            fname=request.POST.get("fname")
            lname=request.POST.get("lname")
            email = request.POST.get("email")
            phone_number = request.POST.get("phone_number")
            pincode= request.POST.get("pincode")
            address = request.POST.get("address")
            catagory = request.POST.get("catagory")
            password = request.POST.get("password")
            user = CustomUser.objects.create_user(
                first_name = fname,
                last_name = lname,
                phoneno = phone_number,
                email = email,
                password = password,
                userflag = True,
            )
            user.set_password(password)
            user.save()
            profile = MechanicProfile.objects.create(
                user = user,
                postalcode = int(pincode),
                address = address,
                category = catagory,
                phoneno = phone_number,
                email = email,
                )
            profile.save()
    return render(request, 'register.html')






def registerasmechanic(request):
    return render(request, 'mechanicregistaer.html')
