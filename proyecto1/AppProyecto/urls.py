from django.urls import path

from AppProyecto import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('canciones', views.canciones, name="Canciones"),
    path('cantantes', views.cantantes, name="Cantantes"),
    path('discos', views.discos, name="Discos"),
    path('musicaFormulario', views.musicaFormulario, name="MusicaFormulario"),
    path('cancionFormulario', views.canciones, name="CancionFormulario"),
    path('cantantesFormulario', views.cantantes, name="CantantesFormulario"),
    path('discosFormulario', views.discos, name="DiscosFormulario"),
    path('buscar/', views.buscar),
]