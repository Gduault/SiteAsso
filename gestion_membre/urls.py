from django.urls import path

from . import views

app_name = 'gestion'

urlpatterns = [
    path('', views.ajouterMembre, name='ajouterMembre'),
]