from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import pelicula

def detailpeli(request, pk):
    peli = get_object_or_404(pelicula, id = pk)
    
    return render(request, "posmovis/detail.html",{"peli":peli})