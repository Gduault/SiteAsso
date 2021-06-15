from django.urls import path
from . import views

urlpatterns = [

    # Pour y acceder changer l'url comme ceci http://127.0.0.1:8000/annuaire/general
    path('general/', views.general, name='general'),
    # Pour y acceder changer l'url comme ceci http://127.0.0.1:8000/annuaire/securite
    path('securite/', views.securite, name='securite'),
    # Pour y acceder changer l'url comme ceci http://127.0.0.1:8000/annaire/classique
    path('classique/', views.classique, name='classique'),
]
