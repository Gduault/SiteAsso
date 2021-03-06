from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

#Creation du formualaire d'inscription pour l'utilisateur
class UserForm(UserCreationForm):
    username = forms.CharField(label='Pseudo', widget=forms.TextInput(attrs={'class': 'form-control', }))
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control', }))
    password2 = forms.CharField(label='Confirmer le mot de passe',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
