from django.urls import path, include
from . import views
urlpatterns = [
    path('registerasmechanic/', views.registerasmechanic, name='registerasmechanic'),
    path('register/', views.register, name='register'),
]