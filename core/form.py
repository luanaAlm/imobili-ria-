from django.forms import ModelForm, fields, models
from .models import Imovel
from .models import Cliente


class ImovelForm(ModelForm):
    class Meta:
        model = Imovel
        fields = "__all__"


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
