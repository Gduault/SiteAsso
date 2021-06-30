from django.shortcuts import render
from corp.models import *
from gestion_membre.decorators import allowed_users

# fonction qui permet l'association d'une page avec la base de donnée
def classique(request):
    # recupere tout les éléments de la classe Adhérent
    adherent = Adherent.objects.all()
    # Retourne tout les éléments de la classe Adherent et redirige vers la page 'classique.html'
    return render(request, 'classique.html', {'adherents':adherent})

#Permet de limiter l'accès au Président et à la sécretaire
@allowed_users(allowed_roles='President, Secretaire')
# fonction qui permet l'association d'une page avec la base de donnée
def general(request):
    #recupere tout les éléments de la classe Adherent dans la BDD
    adherent = Adherent.objects.all()
    # Retourne les éléments de la classe Adhérents et redirige vers la page 'général.html'
    return render(request, 'general.html', {'adherents': adherent})

# fonction qui permet l'association d'une page avec la base de donnée
def securite(request):
    # récupère tout les éléments de la classe Adhérent
    adherent = Adherent.objects.all()
    # Retourne les éléments choisis dans la base et redirige vers la page 'securite.html'
    return render(request, 'securite.html', {'adherents':adherent})

# fonction qui permet l'association d'une page avec la base de donnée
def detail(request, id_adh):
    # recupere l'id de la classe Adherent pour la stocké dans une variable
    adh = Adherent.objects.get(id=id_adh)
    # recupere tout les éléments de la classe Adherent
    adhe = Adherent.objects.all().filter(id=id_adh)
    # recupere les éléments de la classe Assurance_complémentaire à l'aide d'une jointure avec l'id de l'adherent
    ac = Assurance_Complementaire.objects.filter(adherent=adh)
    # recupere les éléments de la classe Certif_medical à l'aide d'une jointure avec l'id de l'adherent
    cm = Certif_Medical.objects.filter(adherent=adh)
    # association des variable de classe pour les réutiliser dans le code HTML de la page 'detail.HTML'
    context = {
        'ac': ac,
        'adhe': adhe,
        'cm': cm,
    }
    #Retourne les éléments de la base choisis et redirige vers la page 'detail.html'
    return render(request, 'detail.html', context)
