from django.db import models


class tags18(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre



# Create your models here.
class mayores(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.CharField(max_length=250)
    codigo = models.TextField()
    generos = models.ManyToManyField(tags18, related_name='generos18ss')    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.nombre
    @classmethod
    def aleatorio(cls):
        return cls.objects.order_by('?')