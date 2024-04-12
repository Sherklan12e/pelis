from django.shortcuts import render, redirect
from .forms import Register

def index(request):
    
    return render(request, "index.html")


def registeruser(request):
    if request.method == 'POST':
        forms = Register(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
        
    else:
        forms = Register()
    return render(request , 'login/register.html')