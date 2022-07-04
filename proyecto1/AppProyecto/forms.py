from dis import disco
from django import forms

class MusicaFormulario(forms.Form):

    cancions = forms.CharField()

class CancionFormulario(forms.Form):

    cancion = forms.CharField()
    duracion = forms.CharField()

class CantantesFormulario(forms.Form):

    nombre = forms.CharField()
    grupo = forms.CharField()

class DiscosFormulario(forms.Form):

    disco = forms.CharField()





