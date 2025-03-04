import os 
from django.shortcuts import render, redirect
from .forms import Register
from django.core.paginator import Paginator
from login.models import pelicula, series
from perfil.models import mayores
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from login.encryption_util import *
from django.db.models import Q

def index(request):
    todo = pelicula.objects.all()[:5]
    series_view = series.objects.all()[:5]
    encrypted_todos = []
    for todoss in todo:
        encrypted_todo = {
            'id': todoss.id,
            'encrypt_key': encrypt(todoss.id),
            'nombre': todoss.nombre, 
            'imagen': todoss.imagen,
        }
        encrypted_todos.append(encrypted_todo)
        
    
    context = {
        "encrypted_todos":encrypted_todos,
        "todo":todo,
        "series_view":series_view,
    }
    
    
    print(request.user)
    
    return render(request, "index.html", context)


def registeruser(request):
    if request.method == 'POST':
        forms = Register(request.POST)
        if forms.is_valid():
            
            
            user = forms.save()
            
            
            login(request ,user)
            return redirect('index')
        
    else:
        forms = Register()
    return render(request , 'login/register.html', {'forms':forms})


def Loginuser(request):
    if request.method=='POST':
        forms = AuthenticationForm(request, request.POST)
        if forms.is_valid():
            user = forms.get_user()
            login(request,user)
            return redirect('index')
    else:
        forms = AuthenticationForm()
    return render(request, "login/login.html", {"forms":forms})

def salir(request):
    logout(request)
    
    return redirect("index")



def peliculaspage(request):
    
  
    todos = pelicula.objects.all()
  
    encrypted_todos = []
    for todoss in todos:
        encrypted_todo = {
            'id': todoss.id,
            'encrypt_key': encrypt(todoss.id),
            'nombre': todoss.nombre, 
            'imagen': todoss.imagen,
            'encrypt_key': encrypt(todoss.id),  
        }
        encrypted_todos.append(encrypted_todo)
            
    context = {
        'encrypted_todos':encrypted_todos,
        'todos':todos
    }
    return render(request, 'pages/peliculas.html', context)


def seriespage(request):
    todos = series.objects.all()
    
    context = {
        'todos':todos
    }
    return render(request, 'pages/series.html' , context)

def page18(request):
    todos = mayores.objects.all()
    pagin = Paginator(todos ,20)
    pag_num = request.GET.get('page')
    pag_ob = pagin.get_page(pag_num)
    encrypted_todoss = []
    for todoss in pag_ob:
        encrypted_todo = {
            'id': todoss.id,
            'encrypt_key': encrypt(todoss.id),
            'nombre': todoss.nombre, 
            'imagen': todoss.imagen,
            'encrypt_key': encrypt(todoss.id),  
        }
        encrypted_todoss.append(encrypted_todo)
    
    context = {
        "encrypted_todoss":encrypted_todoss,
        "pag_ob":pag_ob
    }
    return render(request, 'pages/page18.html', context)

def buscar(request):
    query = request.GET.get('q', '')
    if query:
        # Búsqueda en películas
        peliculas = pelicula.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query)
        )
        
        # Búsqueda en series
        series_results = series.objects.filter(
            Q(title__icontains=query) |
            Q(descripcion__icontains=query)
        )
        
        # Encriptar IDs de películas para las URLs
        encrypted_peliculas = []
        for peli in peliculas:
            encrypted_peli = {
                'id': peli.id,
                'encrypt_key': encrypt(peli.id),
                'nombre': peli.nombre,
                'imagen': peli.imagen,
                'descripcion': peli.descripcion,
                'tipo': 'pelicula'
            }
            encrypted_peliculas.append(encrypted_peli)
        
        # Preparar resultados de series
        series_list = []
        for serie in series_results:
            series_item = {
                'id': serie.id,
                'nombre': serie.title,
                'imagen': serie.portada,
                'descripcion': serie.descripcion,
                'tipo': 'serie'
            }
            series_list.append(series_item)

    else:
        encrypted_peliculas = []
        series_list = []

    context = {
        'query': query,
        'peliculas': encrypted_peliculas,
        'series': series_list,
        'total_results': len(encrypted_peliculas) + len(series_list)
    }
    
    return render(request, 'pages/resultados_busqueda.html', context)

