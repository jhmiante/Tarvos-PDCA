from datetime import date
from django import forms

from pdca.models import PDCA


class IncluirPdcaForm(forms.Form):
    objetivo = forms.CharField(label='Objetivo')
    inicio = forms.DateTimeField(label='Inicio')
    fim = forms.DateTimeField(label='Fim')
    quem = forms.CharField(label='Quem?')
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea())

    def cadastrar(self, usuario):
        objetivo = self.cleaned_data['objetivo']
        inicio = self.cleaned_data['inicio']
        fim = self.cleaned_data['fim']
        quem = self.cleaned_data['quem']
        descricao = self.cleaned_data['descricao']

        PDCA(
            usuario=usuario.user,
            objetivo=objetivo,
            data=date.today(),
            inicio=inicio,
            fim=fim,
            quem=quem,
            descricao=descricao
        ).save()



