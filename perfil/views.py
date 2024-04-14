import os
from django.shortcuts import render, redirect
from posmovis.models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import Editarform
def view_profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, "profile/perfil.html", {"profile": profile})

def editarperfil(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        forms = Editarform(request.POST, request.FILES, instance=profile)
        if profile.imagen:
                os.remove(profile.imagen.path)
        if forms.is_valid():
            forms.save()
            return redirect('profile', username=request.user.username)
    else:
        forms = Editarform(instance=profile)
    return render(request, 'profile/editar.html', {"forms": forms})