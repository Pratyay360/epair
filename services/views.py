from django.shortcuts import render, redirect
from .models import services, Message
from django.utils import timezone
from django.contrib import auth
from django.http import HttpResponse, request
from epair.settings import url,headers
import requests
import json
import random
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/login')
def ac(request):
    params={
        'Service':'Ac'
    }
    return render(request, 'form.html', params)
@login_required(login_url='/login/login')
def fridge(request):
    params={
        'Service':'Fridge'
    }
    return render(request, 'form.html', params)
@login_required(login_url='/login/login')
def computer(request):
    params={
        'Service':'Computer'
    }
    return render(request, 'form.html', params)
@login_required(login_url='/login/login')
def tv(request):
    params={
        'Service':'Tv'
    }
    return render(request, 'form.html', params)
@login_required(login_url='/login/login')
def laptop(request):
    params={
        'Service':'Laptop'
    }
    return render(request, 'form.html', params)
@login_required(login_url='/login/login')
def phone(request):
    params={
        'Service':'Phone'
    }
    return render(request, 'form.html', params)
@login_required(login_url='/login/login')
def electrician(request):
    params={
        'Service':'Electrician'
    }
    return render(request, 'form.html', params)
@login_required(login_url='/login/login')
def plumbing(request):
    params={
        'Service':'Plumber'
    }
    return render(request, 'form.html', params)
@login_required(login_url='/login/login')
def carpenter(request):
    params={
        'Service':'Carpenter'
    }
    return render(request, 'form.html', params)
@login_required(login_url='/login/login')
def electrical(request):
    params={
        'Service':'Electrical'
    }
    return render(request, 'form.html', params)
@login_required(login_url='/login/login')
def other(request):
    params={
        'Service':'Others'
    }
    return render(request, 'form.html', params)

@login_required(login_url='/login/login')
def success(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        desc = request.POST.get('desc')
        catagory = request.POST.get('catagory')
       
        Form = services(name=name, email=email, phone=phone, address=address, pincode=pincode, desc=desc, catagory=catagory, date=timezone.now())
        Form.save()
        Message.objects.create(
            phone=phone
            
        )
        payload = "sender_id=IMPSMS&language=english&route=qt&numbers="+str(phone)+"&message=38038&variables={#EE#}|{#CC#}&variables_values="+name+"|"+catagory
        #model
        # https://www.fast2sms.com/dev/quick-templates?authorization=Vn58qKqlPWdEydvR3Nivaazt8Ril0xNhlwan08zIp2HMHCVIHELQICHKlApP
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
    return render(request, 'success.html')


