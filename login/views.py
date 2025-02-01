from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import pelicula
from posmovis.models import Comment
from posmovis.forms import CommentForm
from django.contrib.auth.decorators import login_required
from .encryption_util import *
from django.contrib.contenttypes.models import ContentType

def detailpeli(request, pk):
    
    pk = decrypt(pk)
    peli = get_object_or_404(pelicula, id = pk)
    incr = encrypt(peli.id)
    
    content_ty = ContentType.objects.get_for_model(pelicula)
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
            return redirect('detailpeli', incr)
    else:
        formscoment = CommentForm()
        
        
    todosloscomentarios = Comment.objects.filter(contentype=content_ty, object_id=peli.id)
    
    
    
    #Esto es para peliculas relacionas con ese genero
    relaciones = pelicula.objects.filter(genero=peli.genero)
    relaciones_todos = []
    for todoss in relaciones:
        encrypted_todo = {
            'id': todoss.id,
            'encrypt_key': encrypt(todoss.id),
            'nombre': todoss.nombre, 
            'imagen': todoss.imagen,
            'encrypt_key': encrypt(todoss.id),  
        }
        relaciones_todos.append(encrypted_todo)
            
    
            
    
    
    context= {
        "incr":incr,
        "relaciones_todos":relaciones_todos,
        "peli":peli,
        "formscoment":formscoment,
        "todosloscomentarios":todosloscomentarios,
        "relaciones":relaciones
    }
    print(encrypt(peli.id))
    print(todosloscomentarios)
    return render(request, "posmovis/detail.html",context)


@login_required()
def megusta(request,pk):
    
    movilike = get_object_or_404(pelicula, id=pk)
    movilike.like +=1
    movilike.save()
    
    return redirect("detailpeli", pk=pk)

@login_required()
def nomegusta(request, pk):
    movidislike = get_object_or_404(pelicula, id=pk)
    movidislike.dislike  += 1
    movidislike.save()
    
    return redirect("detailpeli", pk=pk)

# def error_404_view(request, exception):
#     context = {}
#     return render(request, '404.html', context)

@login_required()
def eliminarcomentario(request, peliid, comen):
    comentario_id = decrypt(peliid)
    comen = get_object_or_404(Comment, id=comen)
    
    if request.method == 'POST':
        comen.delete()
        return redirect('detailpeli', pk=peliid)
    return redirect('detailpeli', pk=peliid)

@login_required()
def eliminarcomentario18(request, peliid18, comen):
    comentario_id = decrypt(peliid18)
    comen = get_object_or_404(Comment, id=comen)
    
    if request.method == 'POST':
        comen.delete()
        return redirect('detail18', pk=peliid18)
    return redirect('detail18', pk=peliid18)
