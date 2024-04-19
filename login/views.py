from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import pelicula
from posmovis.models import Comment
from posmovis.forms import CommentForm

def detailpeli(request, pk):
    peli = get_object_or_404(pelicula, id = pk)
    if request.method=='POST':
        formscoment = CommentForm(request.POST)
        if formscoment.is_valid():
            comentario = formscoment.save(commit=False)
            if request.user.is_authenticated:
                comentario.author = request.user
            else:
                return redirect('login')
            comentario.post = peli
            comentario.save()
            return redirect('detailpeli', pk=pk)
    else:
        formscoment = CommentForm()
    todosloscomentarios = Comment.objects.filter(post=peli.id)
    
    context= {
        "peli":peli,
        "formscoment":formscoment,
        "todosloscomentarios":todosloscomentarios
    }
    print(peli.id)
    print(todosloscomentarios)
    return render(request, "posmovis/detail.html",context)



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

def eliminarcomentario(request, peliid, comen):
    peli = get_object_or_404(pelicula, id=peliid)
    comen = get_object_or_404(Comment, id=comen ,post=peli )
    
    if request.method=='POST':
        comen.delete()
        return redirect( 'detailpeli' , pk=peliid)
    return redirect('detailpeli', pk=peliid)