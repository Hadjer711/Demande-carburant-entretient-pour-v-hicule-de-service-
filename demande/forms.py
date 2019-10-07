from django.forms import ModelForm, RadioSelect, TextInput

from .models import Carburant, Entretient


class CarburantForm(ModelForm):
    class Meta:
        model = Carburant
        fields = '__all__'
        widgets={
            'alimentation': RadioSelect,

            'structure ': TextInput(attrs={'Placeholder': 'Structure'}),
            'telephonePv ': TextInput(attrs={'placeholder': 'Num de Tel privé'}),
            'telephoneBr ': TextInput(attrs={'placeholder': 'Num de Tel de bureau'}),
        }




class EntretientForm(ModelForm):
    class Meta:
        model = Entretient
        fields = '__all__'
