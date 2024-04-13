from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from .models import Profile



class Register(forms.Form):
    CHOICES = [
        ('hombre','Hombre'),
        ('mujer','Mujer'),
    ]
    username = forms.CharField(max_length=250)
    password1 = forms.CharField(label='password' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='repet password !' , widget=forms.PasswordInput)
    sexo = forms.ChoiceField(choices=CHOICES, label='Sexo')
    country = CountryField()
    email = forms.EmailField(required=True)
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