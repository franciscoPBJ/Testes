from django.forms import ModelForm

from app.models import Sales

class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['cidade','endereço','ano']