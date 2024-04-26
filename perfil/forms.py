from django import forms
from posmovis.models import Profile


class Editarform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['imagen', 'sexo','country']