from cProfile import label
from tkinter import Widget
from django import forms
from .models import Categoria, Noticias, Regiones, Contacto
from crispy_forms.helper import FormHelper
from tinymce.widgets import TinyMCE
from phonenumber_field.formfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

# Si se desea todo:
# fields = '__all__'


class EscribirForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = 'escr'
        # self.helper.form_show_labels = False
    titulo = forms.CharField(
        min_length=10,
        max_length=100,
        required=True,
        label='Titulo',
    )
    
    portada = forms.ImageField(
        label='Imagen de Portada',
        widget=forms.FileInput(attrs={'class': 'form-control-file','accept':'image/png, image/jpeg, image/jpg'}),	
    )    
    
    categoria = forms.ModelChoiceField(
        label='',
        empty_label='Categoría', 
        queryset=Categoria.objects, 
        required=True
        )
    ubicacion = forms.ModelChoiceField(
        label='',
        empty_label='Ubicación',
        queryset=Regiones.objects, 
        required=True)
    contenido = forms.CharField(
        label='',
        widget=TinyMCE(attrs={'cols': 80, 'rows': 30,'placeholder':'Escribe aquí tu noticia'}),
    )
    class Meta:
        model = Noticias
        fields = ['titulo', 'portada', 'categoria',
                  'ubicacion', 'contenido', 'etiquetas']
       
class ContactoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = 'cont'
        
        pnombre = forms.CharField(
            min_length= 5,
            max_length=50,
            label='Nombre',
            required=True,
            error_messages={'required': 'El campo es requerido', 'min_length': 'El nombre debe tener al menos 5 caracteres'},
        )
        appaterno = forms.CharField(
            min_length= 5,
            max_length=50,
            label='Apellido',
            required=True,
            error_messages={'required': 'El apellido es obligatorio', 'min_length': 'El apellido debe tener al menos 5 caracteres'},
        )
        email = forms.EmailField(
            required=True,
            label='Email',
            min_length=5,
            error_messages={'invalid': 'Ingrese un email válido', 'required': 'El email es obligatorio', 'min_length': 'El email debe tener al menos 5 caracteres'},
        )
        telefono = PhoneNumberField(
            widget = forms.TextInput(attrs={'placeholder':'+56912345678'}
            ),
            required=True,
            label=("Teléfono"),
            error_messages= {'required': 'Ingrese un número de teléfono válido'},
        )
        
        mensaje = forms.CharField(
            required=True,
            label='Inserta tu mensaje',
            widget=forms.Textarea(attrs={"rows":3}),
            error_messages={'required': 'Este campo es obligatorio'},
        )
        
        archivo = forms.FileField(
            label='',
            widget=forms.FileInput(attrs={'class': 'form-control-file','accept':'image/*,.pdf,doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt,.csv,.zip,.rar'}),
            error_messages={'invalid': 'Formato de archivo no válido'},
            required=False
        )
    class Meta:
        model = Contacto
        fields = ['pnombre', 'appaterno', 'email',
                  'telefono', 'mensaje', 'archivo']
        labels = {
            'pnombre': ('Nombre'),
            'appaterno': ('Apellido'),
            'email': ('Email'),
            'telefono': ('Teléfono'),
            'mensaje': ('Inserta tu mensaje'),
            'archivo': (''),
        }
        help_texts = {
            'archivo': ('Este campo es opcional.'),
        }