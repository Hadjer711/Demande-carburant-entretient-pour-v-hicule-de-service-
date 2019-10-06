"""Demande URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from demande.views import  carburant_affiche, carburant_save,entretient_save ,entretient_affiche, welcome,\
    error404, forgot_psw , welcome_admin, rapport_mensuel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', welcome),
    path('client/carburant/', carburant_save),
    path('client/entretient/', entretient_save),
    path('carburant-affiche/', carburant_affiche),
    path('entretient-affiche/', entretient_affiche),
    path('error404/', error404),
    path('forgot_psw/', forgot_psw),

    path('login/welcome_admin/', welcome_admin),
    path('rapport/', rapport_mensuel),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view() , name='logout'),



]
