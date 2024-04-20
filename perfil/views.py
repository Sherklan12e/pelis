import os
from django.shortcuts import render, redirect
from posmovis.models import Profile
from .models import mayores
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import Editarform
from login.encryption_util import *
from django.contrib.auth.decorators import login_required
from login.encryption_util import *
def view_profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
   
    
    
    return render(request, "profile/perfil.html", {"profile": profile})


@login_required()
def editarperfil(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        forms = Editarform(request.POST, request.FILES, instance=profile)
        if profile.imagen == True:
                os.remove(profile.imagen.path)
        else:   
            if forms.is_valid():
                forms.save()
                return redirect('profile', username=request.user.username)
    else:
        forms = Editarform(instance=profile)
    return render(request, 'profile/editar.html', {"forms": forms})

def detail18(request, pk):
    
    pk = decrypt(pk)
    pos = get_object_or_404(mayores , id=pk)
    
    al = mayores.aleatorio()[:5]
    aleatorio1 = []
    for todoss in al:
        encrypted_todo = {
            'id': todoss.id,
            'encrypt_key': encrypt(todoss.id),
            'nombre': todoss.nombre, 
            'imagen': todoss.imagen,
            'encrypt_key': encrypt(todoss.id),  
        }
        aleatorio1.append(encrypted_todo)
        
    
    so = mayores.aleatorio().exclude(id__in=[item.id for item in al])[:12]
    aleatorio2 = []
    for todoss in so:
        encrypted_todo = {
            'id': todoss.id,
            'encrypt_key': encrypt(todoss.id),
            'nombre': todoss.nombre, 
            'imagen': todoss.imagen,
            'encrypt_key': encrypt(todoss.id),  
        }
        aleatorio2.append(encrypted_todo)
        
        
    context = {
        'aleatorio1':aleatorio1,
        'aleatorio2':aleatorio2,
        'so':so,
        'pos':pos,
        'al':al
    }
    return render(request, 'pages/detail18.html', context)