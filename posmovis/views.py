import os 
from django.shortcuts import render, redirect
from .forms import Register

from login.models import pelicula, series
from perfil.models import mayores
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from login.encryption_util import *
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
    todos = mayores.objects.all()[:20]
    encrypted_todoss = []
    for todoss in todos:
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
        "todos":todos
    }
    return render(request, 'pages/page18.html', context)

