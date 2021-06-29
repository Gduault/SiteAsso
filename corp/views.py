from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from corp.models import Adherent, Assurance_Complementaire, Certif_Medical


@login_required
def index(request):
    current_user = request.user
    user_id = current_user.id
    context = {
        'user_id': user_id,

    }
    return render(request, 'index.html', context)


