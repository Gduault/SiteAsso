from django import forms
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render

from corp.models import Adherent


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', }))




