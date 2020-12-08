
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    #login
    path('login/', views.loginn, name='login'),
    #signup
    path('signup/', views.signup, name='signup'),
    #logut
    path('logout/',views.logout, name='logout'),
    #Foret Password
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(template_name='password_chng.html'),
    ),
    
]