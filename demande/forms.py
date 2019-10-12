from django.forms import ModelForm, RadioSelect, TextInput, DateInput

from .models import Carburant, Entretient, TraitementCarburant


class CarburantForm(ModelForm):
    class Meta:
        model = Carburant
        exclude = ['traite', 'id']
        widgets={
            'alimentation': RadioSelect,

            'structure ': TextInput(attrs={'Placeholder': 'Structure'}),
            'telephonePv ': TextInput(attrs={'placeholder': 'Num de Tel privé'}),
            'telephoneBr ': TextInput(attrs={'placeholder': 'Num de Tel de bureau'}),
        }




class EntretientForm(ModelForm):
    class Meta:
        model = Entretient
        exclude = ['traite', 'id']


class CarburantTraitement(ModelForm):
    class Meta:
        model= TraitementCarburant
        fields = "__all__"
        widgets={
            'dateAlimentation': DateInput(attrs={'type':'date'}),
        }
