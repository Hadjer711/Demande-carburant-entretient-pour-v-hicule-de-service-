from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render

from .forms import CarburantForm, EntretientForm, CarburantTraitement
from .models import Carburant, Entretient, TraitementCarburant


# Create your views here.


def welcome(request):
    template_name='client.html'
    return render(request , template_name )

@login_required
def welcome_admin(request):
    template_name='index.html'
    nb_carb=Carburant.objects.all().filter(traite=False).count()
    nb_carbt=Carburant.objects.all().filter(traite=True).count()
    nb_entr=Entretient.objects.all().filter(traite=False).count()
    nb_entrt=Entretient.objects.all().filter(traite=True).count()
    context = {'nb_carb': nb_carb, 'nb_carbt': nb_carbt, 'nb_entr': nb_entr, 'nb_entrt':nb_entrt}
    return render(request , template_name, context )

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
    query_results=Carburant.objects.all().filter(traite=False)
    template_name='tables2.html'
    context={"query_results":query_results}
    return render(request , template_name ,context)

@login_required
def carburant_traffiche(request):
    query_results=Carburant.objects.all().filter(traite=True)
    template_name='tables2.html'
    context={"query_results":query_results}
    return render(request , template_name ,context)

@login_required
def entretient_affiche(request):
    query_results=Entretient.objects.all().filter(traite=False)
    template_name='tables.html'
    context={"query_results":query_results}
    return render(request , template_name ,context)

@login_required
def entretient_traffiche(request):
    query_results=Entretient.objects.all().filter(traite=True)
    template_name='tables.html'
    context={"query_results":query_results}
    return render(request , template_name ,context)

@login_required
def carburant_traitement(request, id):
    form = CarburantTraitement(request.POST or None)
    result= Carburant.objects.get(id=id)
    if form.is_valid():
        obj = TraitementCarburant.objects.create(**form.cleaned_data)
        obj.save()
        form = CarburantTraitement()
        #print('data valid')
    else:
        print('data is not valid')
    context = {'form': form, 'result':result}
    template_name = 'traitement-Carburant.html'
    return render(request, template_name, context)

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


def logoutTlogin(request):
    return logout_then_login(request, login_url='/login')
