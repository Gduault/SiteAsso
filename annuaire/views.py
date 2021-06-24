from django.shortcuts import render
from corp.models import *


# Create your views here.

# permet d'accéder à la page de la manière suivante http://172.0.0.1/annuaire/classique.html
from gestion_membre.decorators import allowed_users


def classique(request):
    adherent = Adherent.objects.all()
    return render(request, 'classique.html', {'adherents':adherent})

@allowed_users(allowed_roles='President')
# permet d'accéder à la page de la manière suivante http://172.0.0.1/annuaire/general.html
def general(request):
    adherent = Adherent.objects.all()
    return render(request, 'general.html', {'adherents': adherent})

# permet d'accéder à la page de la manière suivante http://172.0.0.1/annuaire/securite.html
def securite(request):
    adherent = Adherent.objects.all()
    return render(request, 'securite.html', {'adherents':adherent})

def detail(request, id_adh):
    adh = Adherent.objects.get(id=id_adh)
    adhe = Adherent.objects.all()
    ac = Assurance_Complementaire.objects.filter(adherent=adh)
    cm = Certif_Medical.objects.filter(adherent=adh)
    context = {
        'ac': ac,
        'adhe': adhe,
        'cm': cm,
    }
    return render(request, 'detail.html', context)
