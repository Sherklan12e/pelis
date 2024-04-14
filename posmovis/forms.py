from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Profile



class Register(forms.Form):
    CHOICES = [
        ('hombre','Hombre'),
        ('mujer','Mujer'),
    ]
    username = forms.CharField(max_length=250 , label='', widget=forms.TextInput(attrs={'class': 'my-4 w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500', 'placeholder':'nombre'}))
    
    password1 = forms.CharField(label='' , widget=forms.PasswordInput(attrs={'class':'my-4  w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500', 'placeholder':'Contraseña'}))
    
    password2 = forms.CharField(label=''  ,  widget=forms.PasswordInput(attrs={'class':'my-4  w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',  'placeholder':'Confirma contraseña'}))
    
    sexo = forms.ChoiceField(choices=CHOICES, label='' , widget=forms.Select(attrs={'class':'my-4  w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',  'placeholder':'Genero'}))
    
    email = forms.EmailField(required=True ,label='', widget=forms.EmailInput(attrs={'class':'my-4 w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500" placeholder="Ingrese su Correo porfavor', 'placeholder':'Correo'}))
    
    
    
    #modelos 

    def clean_email(self):
        email = self.cleaned_data['email']
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya ha sido creado perra!')
        return email
    def save(self):
        user  = User.objects.create_user(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['email'],
                password=self.cleaned_data['password1'],
            )
        
        profile = Profile.objects.create(
            user=user,
            sexo = self.cleaned_data['sexo']
        )
        
        return user