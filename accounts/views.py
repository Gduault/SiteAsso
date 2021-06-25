from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from corp.models import Adherent

# Pour avoir acces a la gestion de profil il faut etre connecter
@login_required
def gestiondeprofil(request):
    context = {
        'adh': Adherent.objects.all(),
        'Adh_id': 'adh'
    }
    return render(request, 'accounts/gestion_profil.html', context)



