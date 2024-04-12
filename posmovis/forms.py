from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django.contrib.auth.models import User


class Register(UserCreationForm):
    CHOICES = [
        ('hombre','Hombre'),
        ('mujer','Mujer'),
    ]
    sexo = forms.ChoiceField(choices=CHOICES, label='Sexo')
    country = CountryField()
    email = forms.EmailField(required=True)
    class Meta:
        fields = ['username','email','country','sexo','password1','password2','']

    
    def clean_email(self):
        email = self.cleaned_data['data']
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya ha sido creado perra!')
        return email