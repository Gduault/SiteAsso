from django import forms
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import render
from django.template.context_processors import request

from corp.models import Adherent


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', }))


class AdherentForm(ModelForm):
    class Meta:
        model = Adherent
        fields = ('NOM', 'PRENOM', 'LIEU_NAISSANCE', 'DATE_NAISSANCE', 'TEL_FIX', 'TEL_PORT',
                  'EMAIL', 'ADD_1', 'ADD_2', 'ADD_3', 'CP', 'VILLE', 'PAYS', 'PER_CONTACT',
                  'NUM_PER_CONTACT', 'MDC_REF')
        labels = {
            'Nom': '',
            'Date de naissance': 'YYYY-MM-DD',
            'Prenom': '',
            'Lieu de naissance': '',
            'Telephone fix': '',
            'Telephone portable': '',
            'Email': '',
            'Adresse 1': '',
            'Adresse 2': '',
            'Adresse 3': '',
            'Code postal': '',
            'Ville': '',
            'Pays': '',
            'Personne a contacter': '',
            'Numero de la personne a contacter': '',
            'Numero de telephone du medecin': '',
            'Nom medecin referent': '',

        }
        widgets = {
            'Nom': forms.TextInput(attrs={'class': 'form-control'}),
            'Prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'Date de naissance': forms.TextInput(attrs={'class': 'form-select'}),
            'Lieu de naissance': forms.TextInput(attrs={'class': 'form-select'}),
            'Telephone fix': forms.TextInput(attrs={'class': 'form-control'}),
            'Telephone portable': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'Adresse 1': forms.TextInput(attrs={'class': 'form-control'}),
            'Adresse 2': forms.TextInput(attrs={'class': 'form-control'}),
            'Adresse 3': forms.TextInput(attrs={'class': 'form-control'}),
            'Code postal': forms.TextInput(attrs={'class': 'form-control'}),
            'Ville': forms.TextInput(attrs={'class': 'form-control'}),
            'Pays': forms.TextInput(attrs={'class': 'form-control'}),
            'Personne a contacter': forms.TextInput(attrs={'class': 'form-control'}),
            'Numero de la personne a contacter': forms.TextInput(attrs={'class': 'form-control'}),
            'Numero de telephone du medecin': forms.TextInput(attrs={'class': 'form-control'}),
            'Nom medecin referent': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Creating a form to add an article.

# Creating a form to change an existing article.
