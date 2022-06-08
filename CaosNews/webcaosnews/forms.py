from django import forms
from .models import Categoria, Noticias, Regiones
from crispy_forms.helper import FormHelper
from tinymce.widgets import TinyMCE

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
        label='Imágen de Portada',
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
       
