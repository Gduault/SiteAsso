"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Lien vers le site django administraion,
    # pour y acceder changer l'url comme ceci http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    # Lien vers l'application corp
    # Pour y acceder changer l'url comme ceci http://127.0.0.1:8000/corp/
    path('corp/', include('corp.urls')),
    # Lien vers l'application evenement
    # Pour y acceder changer l'url comme ceci http://127.0.0.1:8000/evenement/
    path('evenement/', include('evenement.urls')),
    # Lien vers l'application annuaire
    # Pour y acceder changer l'url comme ceci http://127.0.0.1:8000/annuaire/
    path('annuaire/', include('annuaire.urls'))
    # Lien vers l'application accounts
    # Pour y acceder changer l'url comme ceci http://127.0.0.1:8000/accounts
    path('accounts/', include('accounts.urls')),
]
