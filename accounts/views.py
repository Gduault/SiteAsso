
from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from django.forms import ModelForm
from corp.models import Adherent
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm


def register(request):
    if request.user.is_authenticated:
        return redirect('corp:index')

    if request.method == 'POST':
        form = UserForm(request.post)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)
