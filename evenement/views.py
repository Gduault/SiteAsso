
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from requests import request


def agenda(request):
    return render(request, 'evenement/index.html')

