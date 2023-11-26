from django.shortcuts import render, redirect, get_object_or_404            
from django.contrib.auth import login, authenticate,login    
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required                   
from django.contrib.auth.views import LogoutView                             
from .models import *
from .forms import * 


@login_required(login_url='login')
def inicio(resquet):   
    return render(resquet,"AppPro/index.html")



def loguin_requerido(request):   
                                     
    if request.method== 'POST':    
                                         
        form=AuthenticationForm(request, data=request.POST)    
         
        if form.is_valid():
             usuario=form.cleaned_data.get('username')
             contrasenia=form.cleaned_data.get('password')
             user=authenticate(username=usuario, password=contrasenia)
             login(request,user)
             return redirect('peli')
        else:
            return render(request, "AppPro/credenciales/login.html", {"form": form, "mensaje": "Formulario no válido. Corrige los errores e inténtalo de nuevo."})
    else:
         form=AuthenticationForm()
         return render(request, "AppPro/credenciales/login.html", { "form":form})  

 

def registro(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            perfil = Perfil(usuario=user, foto_perfil=form.cleaned_data['foto_perfil'], localidad=form.cleaned_data['localidad'], ig=form.cleaned_data['ig'], email=form.cleaned_data['email'])
            perfil.save()
            return redirect('login')
        else:
            if request.POST['password1'] != request.POST['password2']:
                return render(request, 'AppPro/credenciales/registro.html',{'form':form ,"error":'Contraseñas no coinciden'} )
            elif User.objects.filter(username=request.user).exists():
                 return render(request, 'AppPro/credenciales/registro.html', {'form': form, 'error': 'El usuario ya existe'})
            else:
                return render(request, 'AppPro/credenciales/registro.html',{'form':form ,"error":'Contraseña minimo 8 caracteres'} )
                    
    else:   
        form = PerfilForm()

    return render(request, 'AppPro/credenciales/registro.html', {'form': form})



class BotonLogout(LogoutView):
    template_name = 'AppPro/index.html'


@login_required(login_url='login')
def index(request):
    return render(request, 'AppPro/index.html')


@login_required(login_url='login')
def pelicula(request):
    peli=Pelicula.objects.all()
    return render(request,'AppPro/indice.html',{'peli':peli})



@login_required
def perfil(request):
    instancia_perfil = Perfil.objects.get(usuario=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=instancia_perfil)
        if form.is_valid():
            form.save()
    else:
        form = PerfilForm(instance=instancia_perfil)       
    return render(request, 'AppPro\perfil.html', {'form': form, 'perfil': instancia_perfil})



@login_required 
def comentar(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    comentarios = Comentario.objects.filter(pelicula=pelicula)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = Comentario(usuario=request.user, pelicula=pelicula, contenido=form.cleaned_data['contenido'])
            comentario.save()
            comentarios = Comentario.objects.filter(pelicula=pelicula)
            return redirect('comentar', pelicula_id=pelicula_id)
    else:
        form = ComentarioForm()

    return render(request, 'AppPro/detalle_pese.html', {'pelicula': pelicula, 'form': form, 'comentarios': comentarios})


