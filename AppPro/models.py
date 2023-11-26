from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User



class ContenidoAudiovisual(models.Model):
    id = models.AutoField(primary_key=True)
    poster=ImageField(upload_to='AppPro/img',default='AppPro/img/posterdefault.jpg')
    titulo = models.CharField(max_length=255)
    duracion = models.IntegerField()  
    genero = models.CharField(max_length=50)
    sinopsis = models.CharField(max_length=1000, default='Sin sinopsis disponible')
    anio=models.IntegerField(default="0000")

    class Meta:
        abstract = True  # Hace que esta clase sea abstracta y no se cree como una tabla en la base de datos directamente



class Pelicula(ContenidoAudiovisual):
    director = models.CharField(max_length=255)
    


class Serie(ContenidoAudiovisual):
    temporadas = models.IntegerField(max_length=100)
    Capitulos = models.IntegerField(max_length=600)

    

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', default='AppPro/img/avatar.png', blank=True, null=True)
    localidad=models.CharField(max_length=50,null=True,blank=True)
    ig=models.CharField(max_length=50, null=True,blank=True)
    email = models.EmailField(default='ejemplo@ejemplo.com')
    

    def __str__(self):
        return self.usuario.username
    


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    contenido = models.TextField()
    comentario=models.CharField(max_length=1000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username
