from django.db import models

class pelicula(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()