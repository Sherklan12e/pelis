from django.db import models

class Actor(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return  self.nombre
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
    actores = models.ManyToManyField(Actor,related_name='peliculas')
    
            
    def __str__(self):
        return  "Nombre de la pelicula: " + self.nombre 
    
    
    class Meta:
        ordering = ['-id']
    
class series(models.Model):
    
    title = models.CharField(max_length=250)
    portada = models.CharField(max_length=250)
    descripcion  = models.TextField()
    fecha_estreno_serie = models.DateField()
    generos = models.ForeignKey(Genero, on_delete=models.CASCADE , default=1)
    duracion = models.PositiveBigIntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    
    
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.title
    
    
class agregar_cap(models.Model):
    seriea = models.ForeignKey(series, on_delete=models.CASCADE , related_name='partesss')
    title = models.CharField(max_length=240)
    fecha = models.DateField()
    
    codigo_serie = models.TextField()
    
    class Meta:
        ordering = ['id']
    
    
    def __str__(self):
        return self.title