from django.contrib import admin
from .models import pelicula, Genero, series, agregar_cap, Actor

admin.site.register(pelicula)
admin.site.register(Genero)
admin.site.register(series)
admin.site.register(agregar_cap)
admin.site.register(Actor)