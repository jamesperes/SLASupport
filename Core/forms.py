# from django import forms
# from .models import Chamado, Area, Problema
# import json

from django.forms import ModelForm, RadioSelect
from Core.models import Chamado, Problema, Area, Categoria_Problema


class ChamadoForm(ModelForm):

    class Meta:

        model = Chamado
        fields = '__all__'
        widgets = {
            'categoria_problema': RadioSelect()
        }        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['problema'].queryset = Problema.objects.none()
        if 'area' in self.data:
            try:
                area_id = int(self.data.get('area'))
                self.fields['problema'].queryset = Problema.objects.filter(
                    area_id=area_id).order_by('desc_problema')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['problema'].queryset = self.instance.area.problema_set.order_by('desc_problema')

        self.fields['categoria_problema'].queryset = Categoria_Problema.objects.none()

        if 'problema' in self.data:
            try:
                problema_id = int(self.data.get('problema'))
                self.fields['categoria_problema'].queryset = Categoria_Problema.objects.filter(problema_id=problema_id).order_by('desc_categoria_problema')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['categoria_problema'].queryset = self.instance.problema.categoria_problema_set.order_by('desc_categoria_problema')
