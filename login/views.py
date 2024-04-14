from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import pelicula 

def detailpeli(request, pk):
    peli = get_object_or_404(pelicula, id = pk)
    
    return render(request, "posmovis/detail.html",{"peli":peli})



def megusta(request,pk):
    movilike = get_object_or_404(pelicula, id=pk)
    movilike.like +=1
    movilike.save()
    
    return redirect("detailpeli", pk=pk)


def nomegusta(request, pk):
    movidislike = get_object_or_404(pelicula, id=pk)
    movidislike.dislike  += 1
    movidislike.save()
    
    return redirect("detailpeli", pk=pk)

def error_404_view(request, exception):
    return render(request, '404.html', status=404)