from django import forms
from .models import Elemento,Atributo,Vulnerabilidad,Inspector,ModoDeFalla,Inspeccion,Foto

class ElementoForm(forms.ModelForm):
    class Meta:
        model= Elemento
        fields=['nombre','descripcion','padre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'padre': forms.Select(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'nombre': {
                'unique': "Este nombre ya está en uso. Por favor, elija otro.",
                'required': "El nombre es obligatorio.",
            },
            'descripcion': {
                'required': "La descripción es obligatoria.",
            },
            'padre': {
                'required': "Debe seleccionar un padre.",
            }
        }


class AtributoForm(forms.ModelForm):
    class Meta:
        model= Atributo
        fields=['nombre','descripcion','tag','elemento']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'elemento': forms.Select(attrs={'class': 'form-control'}),
        }


class VulnerabilidadForm(forms.ModelForm):
    class Meta:
        model= Vulnerabilidad
        fields=['nombre','valor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class InspectorForm(forms.ModelForm):
    class Meta:
        model=Inspector
        fields=['nombre','mail']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control','type':"email"})
        }      

class ModoDeFallaForm(forms.ModelForm):
    class Meta:
        model=ModoDeFalla
        fields=['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }

class InspeccionForm(forms.ModelForm):
    class Meta:
        model = Inspeccion
        fields = ['fecha', 'inspector', 'atributo', 'vulnerabilidad', 'temperatura', 'vibracion', 'observacion', 'aviso', 'modosdefalla']  # Incluir 'fotos' en los campos del formulario
        
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control','type': 'datetime-local'}),
            'inspector': forms.Select(attrs={'class': 'form-control'}),
            'atributo': forms.Select(attrs={'class': 'form-control select2'}),
            'vulnerabilidad': forms.Select(attrs={'class': 'form-control'}),
            'temperatura': forms.NumberInput(attrs={'class': 'form-control'}),
            'vibracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
            'aviso': forms.TextInput(attrs={'class': 'form-control'}),
            'modosdefalla': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class FotoForm(forms.Form):

    imagenes = forms.ImageField(required=False)
    widgets = {
            'imagenes': forms.ClearableFileInput(attrs={'class': 'form-control-file','multiple': True}),
        }