from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def privacy(request):
    return render(request, 'privacy.html')
    
def done(request):
    return render(request, 'password_change_done.html')
    