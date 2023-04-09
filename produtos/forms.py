from django import forms
from .models import Produtos

class ProdutoForm(forms.ModelForm):
    class Meta: 
        model = Produtos
        fields = ['cod_prod', 'nome', 'descricao', 'barra', 'valor', 'estoque']
        labels = {
            'cod_prod': 'Codigo Produto',
            'nome': 'Nome',
            'descricao': 'Descricao',
            'barra': 'Barra',
            'valor': 'Valor',
            'estoque': 'Estoque'
        }
        widgets = {
            'cod_prod': forms.NumberInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao':forms.TextInput(attrs={'class': 'form-control'}),
            'barra':forms.TextInput(attrs={'class': 'form-control'}),
            'valor':forms.NumberInput(attrs={'class': 'form-control'}),
            'estoque':forms.NumberInput(attrs={'class': 'form-control'})
        }