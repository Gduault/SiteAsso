from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import AdherentForm
from corp.models import Adherent


# Pour avoir acces a la gestion de profil il faut etre connecter



def update_adherent(request, id_adh):
    adh = Adherent.objects.get(id=id_adh)
    form = AdherentForm(request.POST or None, instance=adh)
    if form.is_valid():
        form.save()
        return redirect('corp:index')
    context = {
        'adh': adh,
        'form': form,
    }
    return render(request, 'accounts/gestion_profil.html', context)
