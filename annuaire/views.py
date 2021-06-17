from django.shortcuts import render
from corp.models import *


# Create your views here.

# permet d'accéder à la page de la manière suivante http://172.0.0.1/annuaire/classique.html
def classique(request):
    adherent = Adherent.objects.all()
    return render(request, 'classique.html', {'adherents':adherent})


# permet d'accéder à la page de la manière suivante http://172.0.0.1/annuaire/general.html
def general(request):
    adherent = Adherent.objects.all()
    return render(request, 'general.html', {'adherents': adherent})

# permet d'accéder à la page de la manière suivante http://172.0.0.1/annuaire/securite.html
def securite(request):
    adherent = Adherent.objects.all()
    return render(request, 'securite.html', {'adherents':adherent})
