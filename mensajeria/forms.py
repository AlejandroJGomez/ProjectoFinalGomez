from django import forms
from django.contrib.auth.models import User




class FormularioIniciarConversacion(forms.Form):
    user_chat_2 = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label='',
        label='Chatear con',
        to_field_name='username',
        widget=forms.Select(attrs={'class': 'form-select'})
        
        
        )



class FormularioEnvioMensaje(forms.Form):

    contenido = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={ 'class' : 'form-control' }),
        label=''
    )
