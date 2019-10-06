from django.forms import ModelForm, RadioSelect

from .models import Carburant, Entretient

class CarburantForm(ModelForm):
    class Meta:
        model = Carburant
        fields = '__all__'
        widgets={
            'alimentation': RadioSelect
        }




class EntretientForm(ModelForm):
    class Meta:
        model = Entretient
        fields = '__all__'
