import os
from django import forms
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from .models import Profile ,Comment

from birthday import BirthdayField, BirthdayManager

class Register(forms.Form):
    CHOICES = [
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
    ]
    username = forms.CharField(max_length=250, label='', widget=forms.TextInput(attrs={'class': 'my-4 w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500', 'placeholder': 'Nombre'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'my-4 w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'my-4 w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500', 'placeholder': 'Confirma contraseña'}))
    sexo = forms.ChoiceField(choices=CHOICES, label='', widget=forms.Select(attrs={'class': 'my-4 w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500', 'placeholder': 'Género'}))
    email = forms.EmailField(required=True, label='', widget=forms.EmailInput(attrs={'class': 'my-4 w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500', 'placeholder': 'Correo'}))
    country = CountryField().formfield(label='', widget=forms.Select(attrs={'class': 'my-4 w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500', 'placeholder': 'País'}))
    edad = forms.DateField( required=True ,label='',
        widget=forms.DateInput(
            attrs={
            'class':"my-4 w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500",
            'type':"date"
            }
        )
    )
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya ha sido registrado.')
        return email

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
        )
        path_imag = os.path.join('static','user.jpg')
        profile = Profile.objects.create(
            user=user,
            sexo=self.cleaned_data['sexo'],
            country=self.cleaned_data['country'],
            imagen = path_imag,
            edad = self.cleaned_data['edad']
            
        )
        return user


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text':''
        }
        widgets = { 
            'text': forms.Textarea( attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500 mb-4', 'placeholder':'Escribe un comentario aqui bro' })}