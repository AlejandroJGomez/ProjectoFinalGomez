from django.urls import path, include
from .views import *





app_name="apppro"
urlpatterns = [
    
    path('',inicio, name= "inicio"),
    path('login/',loguin_requerido, name="login"),
    path('registro/',registro, name="registro"),
    path('logout/', BotonLogout.as_view(template_name='AppPro/index.html'), name="logout"),
    path('indice/',pelicula,name='peli'),
    path('perfil/', perfil, name='perfil'),
    path('detalle/<int:pelicula_id>/', detalles_con_comentarios, name='detalles_con_comentarios'),
    
    ]