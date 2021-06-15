from django.shortcuts import render
from corp.models import *


# Create your views here.

# permet d'accéder à la page de la manière suivante http://172.0.0.1/annuaire/classique.html
def classique(request):
    return render(request, 'classique.html')

# permet d'accéder à la page de la manière suivante http://172.0.0.1/annuaire/general.html
def general(request):
    return render(request, 'general.html')

# permet d'accéder à la page de la manière suivante http://172.0.0.1/annuaire/securite.html
def securite(request):
    return render(request, 'securite.html')
