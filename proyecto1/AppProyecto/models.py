#from mailbox import NoSuchMailboxError
from mailbox import NoSuchMailboxError
from django.db import models
from django.forms import DateField

# Create your models here.
class Canciones(models.Model):
    nombre = models.CharField(max_length=30)
    duracion = models.CharField(max_length=10)

class Cantantes(models.Model):
    nombre = models.CharField(max_length=30)
    grupo = models.CharField(max_length=30)

class Discos(models.Model):
    nombre = models.CharField(max_length=30)


