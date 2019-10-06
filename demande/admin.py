from django.contrib import admin

# Register your models here.
from .models import Entretient, Carburant

admin.site.register(Entretient)
admin.site.register(Carburant)