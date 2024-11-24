from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_finalizacion = models.DateTimeField(null=True, blank = True)
    importante = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + '-by ' + self.user.username

class Project (models.model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_de_creacion = models.DateTimeFieldTimeField(auto_now_add=True)
    fecha_de_finalizacion = models.DateTimeField(null= True, blank = True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + '-by ' + self.user.username





