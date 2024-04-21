import os
from django.shortcuts import render, redirect
from posmovis.models import Profile,Comment
from posmovis.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from .models import mayores
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import Editarform
from login.encryption_util import *
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator

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
        
        
        
        
        
     
    incr = encrypt(pos.id)
    #COMENTARIO
    content_ty = ContentType.objects.get_for_model(mayores)
    if request.method=='POST':
        formscoment = CommentForm(request.POST)
        if formscoment.is_valid():
            comentario = formscoment.save(commit=False)
            if request.user.is_authenticated:
                comentario.author = request.user
            else:
                return redirect('login')
            comentario.contentype = content_ty
            comentario.object_id = pk
            comentario.save()
            
            return redirect('detail18', incr)
    else:
        formscoment = CommentForm()
        
        
    todosloscomentarios = Comment.objects.filter(contentype=content_ty, object_id=pos.id)
    
    
        
    context = {
        'aleatorio1':aleatorio1,
        'aleatorio2':aleatorio2,
        'todosloscomentarios':todosloscomentarios,
        'so':so,
        'formscoment':formscoment,
        'incr':incr,
        'pos':pos,
        'al':al
    }
    return render(request, 'pages/detail18.html', context)