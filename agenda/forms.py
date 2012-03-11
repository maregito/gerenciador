#-*- coding: utf-8 -*-

from django.forms import ModelForm
from agenda.models import ItemAgenda
from django import forms

class FormItemAgenda(forms.ModelForm):
    
    class Meta:
        model = ItemAgenda
        fields = ('nome', 'sobrenome', 'sexo', 'endereco', 'numero', 'bairro', 'cidade', 'estado', 'telefone', 'celular', 'nascimento', 'email', 'rg', 'cpf', 'mae', 'pai', 'civil', 'deficiencia', 'beneficio', 'valor', 'moradia', 'ncomodos', 'scomodos', 'valuguel', 'terreno', 'areaHab', 'esgoto', 'encanada', 'membros', 'renda', 'respesa', 'medicamento', 'profissao', 'possuiNegocio', 'situacaoNego', 'fpam')
