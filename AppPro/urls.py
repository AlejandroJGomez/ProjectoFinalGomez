
from django.urls import path, include
from .views import *


urlpatterns = [
    
    path('',inicio, name= "inicio"),
    path('login/',loguin_requerido, name="login"),
    path('registro/',registro, name="registro"),
    path('logout/', BotonLogout.as_view(template_name='AppPro/index.html'), name="logout"),
    path('indice/',pelicula,name='peli'),
    path('perfil/', perfil, name='perfil'),
    path('comentar/<int:pelicula_id>/',comentar, name='comentar'),
    path('series', series, name="series"),
    path('infantiles', infantiles, name="infantiles"),
    path('reseñas', resenias, name="reseñas"),
    path('series', series, name="series"),
    path('nosotros', nosotros, name="nosotros"),
    path('infantiles', infantiles, name="infantiles"),
    path('contactanos', contactanos, name="contactanos"),
    
    path('pelicula/list', PeliculaList.as_view(), name="pelicula_list"),
    ]
