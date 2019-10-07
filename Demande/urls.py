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
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import path

from demande.views import carburant_affiche, carburant_save, entretient_save, entretient_affiche, welcome, \
    error404, forgot_psw, welcome_admin, rapport_mensuel, logoutTlogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', welcome),
    path('client/carburant/', carburant_save),
    path('client/entretient/', entretient_save),
    path('carburants/', carburant_affiche, name='carburants'),
    path('entretients/', entretient_affiche, name='entretients'),
    path('error404/', error404),
    path('forgot_psw/', forgot_psw),

    path('account/', welcome_admin, name='home'),
    path('rapport/', rapport_mensuel, name='rapport'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logoutTlogin, name='logout'),
    path('account/logout/', lambda request: redirect('logout', permanent=False)),
    path('rapport/logout/', lambda request: redirect('logout', permanent=False)),
    path('carburants/logout/', lambda request: redirect('logout', permanent=False)),
    path('entretients/logout/', lambda request: redirect('logout', permanent=False)),
    path('login/welcome_admin/', lambda request: redirect('home', permanent=False)),




]
