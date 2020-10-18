from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import auth, messages
from django.http import HttpResponse, request
from epair.settings import url,headers
import random
from login.models import OTP
from .models import OtpDirectory
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
        try:
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
                #create Otp
                otp=random.randint(111111,999999)
                print(otp)
                OTP.objects.create(
                    phoneno=phoneno,
                    otp=otp 
                )
                payload = "sender_id=IMPSMS&language=english&route=qt&numbers="+str(phoneno)+"&message=38039&variables={#EE#}|{#BB#}&variables_values="+fname+"|"+str(otp)
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                return redirect(f'/login/verify/?ph={phoneno}')
        except:
            return render(request, 'signup.html',{'message':'<div class="alert alert-danger" role="alert">'
                                                            'Error! Check Your Entered Details (Email / Phone Number'
                                                            ' Previously Used)</div>'})

    return render(request, 'signup.html')
#logut
def logout(request):
    auth.logout(request)
    return redirect('/')
#Otp Submition Page 
def otpsubmissionpage(request):
    if request.method == "POST":
        otprecord = OTP.objects.get(phoneno=request.POST.get('phonenumber'))
        if otprecord.otp == int(request.POST.get('otp')):
            ph=request.POST.get('phonenumber')
            customer = CustomUser.objects.get(phoneno=ph)
            customer.verified = True
            customer.save()
            auth.login(request,customer)
            return redirect('/')
        else:
            return render(request, 'otpsubmissionpage.html', {"phoneno": request.GET.get('ph', "Error"),"message":"Try Again ! Enter Corrct OTP"})
    elif request.method == "GET" and request.GET.get('ph',"")!="":
        return render(request,'otpsubmissionpage.html',{"phoneno":request.GET.get('ph',"Error")})
    else:
        return HttpResponse("<h1>404 Not Found !</h1><h3>Something Going Wrong</h3> ",status='404')
#forget password
@csrf_protect
@never_cache
def forgetpass(request):
    if request.user.is_authenticated:
            return redirect('/')
    else:
        if request.method == 'POST':
            if int(request.POST.get('step'))== 1:
                phoneno= request.POST.get('phoneno')
                otp=random.randint(11111,99999)
                try:
                    if CustomUser.objects.get(phoneno=phoneno):
                        OtpDirectory.objects.create(
                            phoneno=phoneno,
                            otp=otp,
                        )
                        # Here I have Used the sms template login. update it later
                        payload = "sender_id=IMPSMS&language=english&route=qt&numbers=" + str(phoneno) + "&message=38169&variables={#BB#}&variables_values=" + str(otp)
                        requests.request("POST", url, data=payload, headers=headers)

                        return render(request,'forgetpass2.html',{"phoneno":phoneno})
                except:
                    return render(request,'forgetpass1.html',{"phoneno":phoneno,"message":'''<div class="alert alert-danger" role="alert">
                    This Number {} Does Not Exsists</div>'''.format(phoneno)})

            elif int(request.POST.get('step'))== 2:
                phoneno= request.POST.get('phoneno')
                otp=request.POST.get('otp')
                if OtpDirectory.objects.filter(phoneno=phoneno).order_by('-id')[0].otp == int(otp):
                    return render(request,'forgetpass3.html',{'phoneno':phoneno})
                else:
                    return render(request,'forgetpass2.html',{"message":'''<div class="alert alert-danger" role="alert">
                    Otp does not match... Please Retry</div>''',"phoneno":phoneno})
            elif int(request.POST.get('step'))== 3:
                phoneno= request.POST.get('phoneno')
                password=request.POST.get('password')
                userr=CustomUser.objects.get(phoneno=phoneno)
                userr.set_password(password)
                userr.save()
                login(request,userr)
                return redirect('/')

    return render(request,'forgetpass1.html')











