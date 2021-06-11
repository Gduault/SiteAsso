#
from django.db.migrations import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def registerPage(request):
    form = UserCreationForm(request.POST)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'login.html', context)

def carousel(request):
    return render(request, 'caroussel.html')
