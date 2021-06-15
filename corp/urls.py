from xml.etree.ElementInclude import include
from . import views
from django.urls import path

app_name = 'corp'

urlpatterns = [
    # Lien du menu
    # Pour y acceder changer l'url comme ceci http://127.0.0.1:8000/corp/
    path('', views.index, name='index'),
    # Lien pour se conneceter au site
    # Pour y acceder changer l'url comme ceci http://127.0.0.1:8000/corp/login/

]
