from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from django.forms import ModelForm

from corp.models import Adherent
from django.contrib.auth.forms import UserCreationForm

from .decorators import allowed_users
from .forms import UserForm

#Acces reservé pour le group Secretaire
@allowed_users(allowed_roles='Secretaire')
#Debut fonction ajouterMembre qui permettre a la secretaire d'ajouter un membre
def ajouterMembre(request):
    global context
    #On teste si la requete est un post
    if request.method == 'POST':
        #On met le formualire dans une variable form
        form = UserForm(request.POST)
        #Si le formulaire est valide
        if form.is_valid():
            #On le sauvegarde
            form.save()
            #On affiche un message pour prevenir l'utilisateur
            messages.success(request, f'Le compte de l''utilisateur à bien été crée')
            #On redirige l'utilisateur vers la page pour ajouter un membre
            return redirect('gestion:ajouterMembre')
    else:
        form = UserForm()
        context = {
            'form': form,
        }
        messages.error(request, f'Le compte de l''utilisateur n''a pas été crée')
    return render(request, 'ajouter_membre.html', context)

def assuranceMembre(request):
    adherent = Adherent.objects.all()

    return render(request, 'Assurance_membre.html', {'adherents': adherent}, )


def licenceMembre(request):
    adherent = Adherent.objects.all()

    return render(request, 'Licence_membre.html', {'adherents': adherent}, )

def gererMembre(request):
    adherent = Adherent.objects.all()

    return render (request, 'Gerer_Membre.html', {'adherents': adherent}, )

