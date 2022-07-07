from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppProyecto.models import Canciones, Cantantes, Discos
from AppProyecto.forms import MusicaFormulario, CancionFormulario, CantantesFormulario, DiscosFormulario
#from django import loader


# Create your views here.
def inicio(request):

    return render(request, "AppProyecto/inicio.html")

#def canciones(request):

    #return render(request, "AppProyecto/canciones.html")

#def cantantes(request):

    #return render(request, "AppProyecto/cantantes.html")

#def discos(request):

    #return render(request, "AppProyecto/discos.html")

#def generos(request):

    #return render(request, "AppProyecto/generos.html")

def musicaFormulario(request):
    
    if request.method == 'POST':

            Formulario = MusicaFormulario(request.POST)

            print(Formulario)

            if Formulario.is_valid:  

                  informacion = Formulario.cleaned_data
                  
                  song = Canciones (nombre=informacion['cancions']) 

                  song.save()

                  return render(request, "AppProyecto/canciones.html") 
                  
    else:
        
        Formulario = MusicaFormulario()
                
    return render(request, "AppProyecto/musicaFormulario.html", {"Formulario":Formulario})

#BUSCADOR

def buscar(request):
    
    if request.POST['grupo']:

        grupo = request.POST['grupo']
        print(grupo)
        cantante = Cantantes.objects.filter(grupo__icontains=grupo)
        print(cantante.values())
        return render(request, "AppProyecto/inicio.html", {"cantantes": cantante.values()})
        

    else:
        respuesta = "No enviaste datos"
    return render(request,"AppProyecto/cantantes.html", {"respuesta":respuesta})

#CANCIONES
def canciones(request):
    
    if request.method == 'POST':

         Formulario1 = CancionFormulario(request.POST)
         print(Formulario1)
         
         if Formulario1.is_valid:
            
            informacion = Formulario1.cleaned_data
            
            cancion = Canciones(nombre=informacion['cancion'], duracion=informacion['duracion'])
            cancion.save()
            
            return render(request, "AppProyecto/inicio.html")
    else:
        
        Formulario1 = CancionFormulario()
    return render(request, "AppProyecto/canciones.html", {"Formulario1":Formulario1})


def cantantes(request):
    
    if request.method == 'POST':
        
        Formulario3 = CantantesFormulario(request.POST)
        print(Formulario3)
        
        if Formulario3.is_valid:
            
            informacion = Formulario3.cleaned_data
            
            cantantes = Cantantes(nombre=informacion['nombre'], grupo=informacion['grupo'])
            cantantes.save()
            
            return render(request, "AppProyecto/inicio.html")
            
    else:
        Formulario3 = CantantesFormulario()
        
        return render(request, "AppProyecto/cantantes.html", {"Formulario3":Formulario3})


 #DISCOS
def discos(request):
    
    if request.method == 'POST':
        
        Formulario5 = DiscosFormulario(request.POST)
        
        print(Formulario5)
        
        if Formulario5.is_valid:
            informacion = Formulario5.cleaned_data
            
            discos = Discos(nombre=informacion['disco'])
            discos.save()
            
            return render(request, "AppProyecto/inicio.html")
        
    else:
        
        Formulario5 = DiscosFormulario() 
    return render(request, "AppProyecto/discos.html", {"Formulario5":Formulario5})
