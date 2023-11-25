from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil, Comentario
from django.contrib.auth.models import User


class PerfilForm(UserCreationForm):
    
    foto_perfil = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}), required=False)
    localidad = forms.CharField(max_length=50, required=False)
    ig = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'foto_perfil', 'localidad', 'ig', 'email']



class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4}),
        }

