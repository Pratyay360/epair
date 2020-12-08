from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import auth, messages
from django.http import HttpResponse, request
import random
import requests
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache

#Login Validation
@csrf_protect
@never_cache
def loginn(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get("log_email")
            password = request.POST.get("log_pass")

            user = auth.authenticate(email=email,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                #Error For Loging With Unknown Details
                messages.info(request, 'Username Or Password Is Incorrect')
                return render(request, 'login.html')

    return render(request, 'login.html')
#Signup validation
@csrf_protect
@never_cache
def signup(request):
    if request.user.is_authenticated:
            return redirect('/')
    else:
        if request.method == 'POST':
            fname = request.POST.get("log_1name")
            lname = request.POST.get("log_sname")
            email = request.POST.get("log_email")
            phoneno = request.POST.get("log_number")
            password = request.POST.get("log_pass")
            user = CustomUser.objects.create_user(
                first_name = fname,
                last_name = lname,
                phoneno = phoneno,
                email = email,
                password = password,
            )
            user.set_password(password)
            user.save()        

    return render(request, 'signup.html')
#logut
def logout(request):
    auth.logout(request)
    return redirect('/')