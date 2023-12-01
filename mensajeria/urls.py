from django.urls import path
from .views import *




urlpatterns = [
    path('verchat', ver_chats, name='ver_chats'),
    path('nuevo/', iniciar_chat, name='nuevo_chat'),
    path('chat/<int:id>/mensajes/', ver_chat, name='ver_chat'),
    
]
