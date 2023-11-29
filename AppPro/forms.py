from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

#Formulario de registro    
class PerfilForm(UserCreationForm):
    foto_perfil = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}), required=False)
    localidad = forms.CharField(max_length=50, required=False)
    ig = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Agrega los campos del modelo User
        # Agrega los campos del modelo Perfil
        fields = ['foto_perfil', 'localidad', 'ig']
        

#Formulario de Edición de perfil
class PerfilEdicionForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto_perfil', 'localidad', 'ig']
        widgets = {
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }
        
        

#Formulario de comentarios
class ComentarioForm(forms.Form):
    contenido=forms.CharField(widget=forms.Textarea)