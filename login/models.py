from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return "nombre de genero: " + self.nombre
class pelicula(models.Model):
    nombre = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100, default="hola")
    imagen = models.CharField(max_length=250) 
    descripcion = models.TextField()
    calificacion = models.DecimalField(max_digits=3,decimal_places=1)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    fecha_de_estreno = models.DateField()
    duracion = models.PositiveBigIntegerField()
    codigo_peli = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return  "Nombre de la pelicula: " + self.nombre 
    
    
    class Meta:
        ordering = ['-nombre']
    