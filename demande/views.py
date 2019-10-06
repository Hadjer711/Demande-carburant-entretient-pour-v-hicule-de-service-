from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .forms import CarburantForm, EntretientForm
from .models import Carburant, Entretient
# Create your views here.

def carburant_create(request):
    obj=Carburant.objects.get(id=1)
    template_name='carburant.html'
    context={"object":obj}
    return render(request,template_name,context)

def welcome(request):
    template_name='client.html'
    return render(request , template_name )

@login_required
def welcome_admin(request):
    template_name='index.html'
    return render(request , template_name )

def login(request):
    template_name='login.html'
    return render(request , template_name )

def forgot_psw(request):
    template_name='forgot-password.html'
    return render(request , template_name )

@login_required
def rapport_mensuel(request):
    template_name='charts.html'
    return render(request , template_name )

def error404(request):
    template_name='404.html'
    return render(request , template_name )

@login_required
def carburant_affiche(request):
    query_results=Carburant.objects.all()
    template_name='tables2.html'
    context={"query_results":query_results}
    return render(request , template_name ,context)

@login_required
def entretient_affiche(request):
    query_results=Entretient.objects.all()
    template_name='tables.html'
    context={"query_results":query_results}
    return render(request , template_name ,context)

def carburant_save(request):
     form = CarburantForm(request.POST or None)
     if form.is_valid():
         obj=Carburant.objects.create(** form.cleaned_data)
         obj.save()
         form = CarburantForm()
         print('data valid')
     else: print('data is not valid')
     context={'form': form}
     template_name = 'carburant.html'
     return render(request, template_name, context)


def entretient_save(request):
    form = EntretientForm(request.POST or None)
    if form.is_valid():
        obj = Entretient.objects.create(**form.cleaned_data)
        obj.save()
        form = EntretientForm()
        print('data valid')
    else:
        print('data is not valid')
    context = {'form': form}
    template_name = 'entretient.html'
    return render(request, template_name, context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        template_name='index.html'
        login(request, user)
        return render(request,template_name)
    else:
        print('login none ')
        return 0

def logout_view(request):
    logout(request)
    template_name='login.html'
    return render(request, template_name)