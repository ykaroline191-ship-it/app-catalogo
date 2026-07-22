from django import forms
from .models import Obra

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ["titulo", "tipo", "ano", "genero", "descricao"]

        labels = {
            "titulo": "Título da obra",
            "tipo": "Tipo da obra",
            "ano": "Ano de lançamento",
            "genero": "Gênero",
            "descricao": "Descrição",
        }
