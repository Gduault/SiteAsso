from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from corp.models import Adherent


@login_required
def gestiondeprofil(request):
    context = {
        'adh': Adherent.objects.all(),
        'Adh_id': 'adh'
    }
    return render(request, 'accounts/gestion_profil.html', context)



