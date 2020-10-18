"""epair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
admin.site.site_header = "Epair.In Admin"
admin.site.site_title = "Epair.In Admin Portal"
admin.site.index_title = "Welcome to Epair.In  Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('success/', views.index, name='success'),
    path('contact/', include('contactus.urls')),
    path('services/', include('services.urls')),
    path('login/', include('login.urls')),
    path('mechanic/', include('mechanic.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
]
