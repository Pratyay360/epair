from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from contactus.models import contact
from django.utils import timezone


# Create your views here.
def contactus(request):
    return render(request, 'contact.html')

def success(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        Contact = contact(name=name, email=email, phone=phone, desc=desc, date=timezone.now())
        Contact.save()

    return render(request, 'success.html')

    
    
    