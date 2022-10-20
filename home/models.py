from django.db import models
from mailbox import NoSuchMailboxError
from unittest.util import _MAX_LENGTH

class Persona(models.Model):
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    edad =  models.IntegerField()
    fecha_nacimiento = models.DateTimeField(null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    
    
