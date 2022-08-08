from django.db import models

# Create your models here.

class Registro(models.Model): #Define la estrutura de nuestra tabla
     nombre = models.TextField() #Texto largo
     matricula = models.CharField(max_length=12) #texto corto
     correo = models.EmailField()
     edad = models.IntegerField()
     nombre_curso = models.TextField(max_length=10)
     created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
     updated = models.DateTimeField(auto_now_add=True)