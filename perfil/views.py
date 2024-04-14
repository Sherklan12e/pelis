from django.shortcuts import render
from posmovis.models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def view_profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, "profile/perfil.html", {"profile": profile})