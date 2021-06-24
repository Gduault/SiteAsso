
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def agenda(request):
    return render(request, 'agenda.html')

