from django import forms
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render

from corp.models import Adherent


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', }))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class AdherentUpdateForm(forms.ModelForm):
    class Meta:
        model = Adherent
        fields = ['NOM','PRENOM','LIEU_NAISSANCE','DATE_NAISSANCE','TEL_FIX','TEL_PORT','EMAIL','ADD_1','ADD_2','ADD_3','CP','VILLE','PAYS','PER_CONTACT','NUM_PER_CONTACT','MDC_REF','NUM_TEL_MDC',]

@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = AdherentUpdateForm()
    context = {
       'u_form': u_form,
       'p_form': p_form
    }
    return render(request, 'accounts/gestion_profil.html', context)