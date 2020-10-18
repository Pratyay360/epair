from django.urls import path, include
from. import views
urlpatterns = [
    path('ac/', views.ac, name='ac'),
    path('fridge/', views.fridge, name='fridge'),
    path('carpenter/', views.carpenter, name='carpenter'),
    path('computer/', views.computer, name='computer'),
    path('laptop/', views.laptop, name='laptop'),
    path('electrical/', views.electrical, name='electrical'),
    path('electrician/', views.electrician, name='electrician'),
    path('other/', views.other, name='other'),
    path('phone/', views.phone, name='phone'),
    path('plumbing/', views.plumbing, name='plumbing'),
    path('laptop/', views.laptop, name='laptop'),
    path('success/', views.success, name='success'),
]
