from django import forms
from .models import Elemento,Equipo,Vulnerabilidad,Inspector,ModoDeFalla,Inspeccion,Foto,Componente,FuenteDeVulnerabilidad

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


class EquipoForm(forms.ModelForm):
    class Meta:
        model= Equipo
        fields=['nombre','descripcion','tag','elemento']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'elemento': forms.Select(attrs={'class': 'form-control'}),
        }


class ComponenteForm(forms.ModelForm):
    class Meta:
        model= Componente
        fields=['nombre','descripcion','equipo','codigosap']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'equipo': forms.Select(attrs={'class': 'form-control select2'}),
            'codigosap': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigosap'].required = False
        self.fields['codigosap'].label="Código SAP"

class VulnerabilidadForm(forms.ModelForm):
    class Meta:
        model= Vulnerabilidad
        fields=['nombre','valor','color']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control','type':'color'})
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
        fields = ['fecha', 'fuentedevulnerabilidad','inspector', 'componente','notificacion','aviso', 'vulnerabilidad', 'temperatura', 'vibracion', 'observacion','recomendacion','modosdefalla','fechaplaneada','comentarios','realizado']  # Incluir 'fotos' en los campos del formulario
        

        widgets = {
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control','type':'datetime-local'}),
            'fuentedevulnerabilidad': forms.Select(attrs={'class': 'form-control select2'}),
            'inspector': forms.Select(attrs={'class': 'form-control'}),
            'componente': forms.Select(attrs={'class': 'form-control select2'}),
            'vulnerabilidad': forms.Select(attrs={'class': 'form-control'}),
            'temperatura': forms.NumberInput(attrs={'class': 'form-control'}),
            'vibracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
            'aviso': forms.TextInput(attrs={'class': 'form-control'}),
            'modosdefalla': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'notificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'recomendacion': forms.Textarea(attrs={'class': 'form-control'}),
            'fechaplaneada': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control'}),
            'realizado': forms.Select(attrs={'class': 'form-control'},choices=[('Si', 'Sí'), ('No', 'No')]),
        }

        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fechaplaneada'].required = False
        self.fields['aviso'].label="Work Order"
        self.fields['fechaplaneada'].label="Fecha Planeada"
        self.fields['fuentedevulnerabilidad'].label="Fuente de Vulnerabilidad"
        self.fields['vulnerabilidad'].label="Probabilidad"


class FotoForm(forms.Form):

    imagenes = forms.ImageField(required=False)
    widgets = {
            'imagenes': forms.ClearableFileInput(attrs={'class': 'form-control','multiple':''}),
        }
    

class FuenteDeVulnerabilidadForm(forms.ModelForm):
    class Meta:
        model=FuenteDeVulnerabilidad
        fields=['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }