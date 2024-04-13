from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Profile



class Register(forms.Form):
    CHOICES = [
        ('hombre','Hombre'),
        ('mujer','Mujer'),
    ]
    username = forms.CharField(max_length=250 , widget=forms.TextInput(attrs={'class': 'f form-control'}))
    password1 = forms.CharField(label='password' , widget=forms.PasswordInput(attrs={'class':'f password1'}))
    password2 = forms.CharField(label='repet password !' , widget=forms.PasswordInput(attrs={'class':'f password2'}))
    sexo = forms.ChoiceField(choices=CHOICES, label='Sexo',widget=forms.Select(attrs={'class':'f sexo-election'}))
    email = forms.EmailField(required=True , widget=forms.EmailInput(attrs={'class':'f emailregister'}))
    
    
    
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