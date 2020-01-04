from django.forms import ModelForm
from .models import Pessoa, Veiculo, Rotativo


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class RotativoForm(ModelForm):
    class Meta:
        model = Rotativo
        fields = '__all__'