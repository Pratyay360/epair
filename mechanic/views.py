from django.shortcuts import render
from datetime import datetime
from login.models import CustomUser, MechanicProfile
from django.shortcuts import render,redirect
from login.models import CustomUser
from .models import Message1
from django.contrib import auth, messages
from django.http import HttpResponse, request
from epair.settings import url,headers
import random
from login.models import OTP
from login.models import OtpDirectory
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
        try:
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
                Message1.objects.create(
                    phoneno= phone_number
                    )
                # model Id To be Change
                payload = "sender_id=IMPSMS&language=english&route=qt&numbers="+str(phone_number)+"&message=38202&variables={#EE#}|{#CC#}&variables_values="+fname+"|"+catagory
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                return redirect('/')
        except:
            return render(request, 'register.html',{'message':'<div class="alert alert-danger" role="alert">'
                                                            'Error! Check Your Entered Details (Email / Phone Number'
                                                            ' Previously Used)</div>'})
    return render(request, 'register.html')






def registerasmechanic(request):
    return render(request, 'mechanicregistaer.html')
