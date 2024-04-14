from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="perfiles/" )
    sexo = models.CharField(max_length=10, choices=[('hombre', 'Hombre'), ('mujer', 'Mujer')], default='otro')
    country = CountryField(default="NZ")
    def __str__(self):
        return self.user.username
