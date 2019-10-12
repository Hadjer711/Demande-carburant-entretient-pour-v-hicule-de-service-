from django.contrib import admin

# Register your models here.
from .models import Entretient, Carburant, TraitementCarburant

admin.site.register(Entretient)
admin.site.register(Carburant)
admin.site.register(TraitementCarburant)