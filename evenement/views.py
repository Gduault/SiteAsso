from django.shortcuts import render

# Create your views here.

def afficheagenda(request):
    return render(request, 'page_agenda.html')