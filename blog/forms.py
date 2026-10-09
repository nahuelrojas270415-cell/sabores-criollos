from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'categoria', 'descripcion', 'ingredientes', 'pasos', 'tiempo', 'dificultad', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Guiso de lentejas de la nona'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Uno por línea:\n500g lentejas\n1 chorizo colorado...'}),
            'pasos': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'tiempo': forms.TextInput(attrs={'class': 'form-control'}),
            'dificultad': forms.Select(choices=[('Fácil','Fácil'),('Media','Media'),('Difícil','Difícil')], attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }