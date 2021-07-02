from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime as date
import datetime
from django.contrib import messages as message
from django.template.context_processors import request

from corp.models import Adherent

# Fichier avec les conditions pour envoyer les notifications et avec les variable de date correspondante

# Difficulter a relier a la bdd



# Create your views here.
def notification(request):
    # je met dans today la date actuelle
    compt = 0
    compt1 = 0
    compt2 = 0
    compt3 = 0
    today = date.now()

    # Variable avec la date d'inscription de la licence
    DLicence = "2020/06/18"  # à remplacer par la donnée correspondante dans la bdd
    # Je dit que le format de la date sera année/mois/jours
    Dlicence = datetime.datetime.strptime(DLicence, "%Y/%m/%d")

    # Variable avec la date d'inscription de la licence +1 ans (pour avoir la date de fin de la licence)
    NLicence = Dlicence + datetime.timedelta(days=365)

    print(today)
    # je met dans alerteLicence la date à partir de quand la notif doit apparaitre
    alerteLicence = NLicence + datetime.timedelta(days=-30)

    # variable avec le debut de la certif medical avec le format année/mois/jours
    Dcertif = "2021/05/18"  # à remplacer par la donnée correspondante dans la bdd
    Dcertif = datetime.datetime.strptime(Dcertif, "%Y/%m/%d")
    # variable avec la fin de la certif medical avec le format année/mois/jours
    Fcertif = "2021/06/30"  # à remplacer par la donnée correspondante dans la bdd
    Fcertif = datetime.datetime.strptime(Fcertif, "%Y/%m/%d")

    # je met dans alerteCertif la date à partir de quand la notif doit apparaitre
    alerteCertif = Fcertif + datetime.timedelta(days=-14)

    # compteur de notification
    NB_NOTIF = 1

    # variable intermédiaire pour enclencher les notifictions et pouvoir integrer le compteur de notification

    compt4 = 1

    # Variable pour ne plus afficher les notifications
    RenouLice = 0
    RenouCertif = 0

    # Variable que le tresorier met a une certaine valeur pour envoyer une notification
    NotifassuranceTresorier = 1  # à lier a un bouton sur la page gestion de membre du tresorier
    # Variable que le tresorier met a une certaine valeur pour envoyer une notification
    NotiflicenceTresorier = 1  # à lier a un bouton sur la page gestion de membre du tresorier

    # condition d'activation des notifications et compteur de notification

    # si le bouton du tresorier dans gestion membre/licence est activer, envoye une notification
    if NotiflicenceTresorier == 1:
        NB_NOTIF = NB_NOTIF + 1
        compt = 1
        # si le bouton du tresorier dans gestion membre/assurance est activer, envoye une notification
    if NotifassuranceTresorier == 1:
        NB_NOTIF = NB_NOTIF + 1
        compt3 = 1
        # si la date du jour est superieur a la date d'alerte licence ( 1ans apres la date d'inscription licence moins 1 mois) envoye une notif
    if today > alerteLicence:
        NB_NOTIF = NB_NOTIF + 1
        compt1 = 1
        # si la date du jour est superieur a la date d'alerte de la certif ( fin de certif moins 2 semaine ) envoye une certif
        # et si la date du jour est inférieur a la date de fin de certif
    if today > alerteCertif:
        if today < Fcertif:
            NB_NOTIF = NB_NOTIF + 1
            compt2 = 1
        # si un des champs Nom, prenom, lieu de naissance, date de  naissance, tel. portable, Email, adresse 1, code postal, ville, pays, personne a contacter, num personne a contacter, medecin reférent ou num tel medecin referent est vide envoye une notif pour dire de remplir les information dans gestion de profile

    context = {
        "Fcertif": Fcertif,
        "NB_NOTIF": NB_NOTIF,
        "compt": compt,
        "compt1": compt1,
        "compt2": compt2,
        "compt3": compt3,
        "compt4": compt4,
        "NotiflicenceTresorier": NotiflicenceTresorier,
        "NotifassuranceTresorier": NotifassuranceTresorier,
        "RenouLice": RenouLice,
        "RenouCertif": RenouCertif,
    }

    return render(request, 'notif/notification.html', context)



