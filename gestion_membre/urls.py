from django.urls import path

from . import views

app_name = 'gestion'

urlpatterns = [
    path('', views.ajouterMembre, name='ajouterMembre'),
    path('assurance/', views.assuranceMembre, name='assuranceMembre'),
    path('licence/', views.licenceMembre, name='licenceMembre'),
]