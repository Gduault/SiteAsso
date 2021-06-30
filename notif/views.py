from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime as date
import datetime
from django.contrib import messages as message
from corp.models import Adherent

# Fichier avec les conditions pour envoyer les notifications et avec les variable de date correspondante

                                # Difficulter a relier a la bdd


# Create your views here.
def notification(request):

    # je met dans today la date actuelle
    today = date.now()

    # Variable avec la date d'inscription de la licence
    DLicence = "2020/06/18"                     # à remplacer par la donnée correspondante dans la bdd
    # Je dit que le format de la date sera année/mois/jours
    Dlicence = datetime.datetime.strptime(DLicence, "%Y/%m/%d")



    # Variable avec la date d'inscription de la licence +1 ans
    NLicence = Dlicence + datetime.timedelta(days=365)



    print(today)
    # je met dans alerteLicence la date à partir de quand la notif doit apparaitre
    alerteLicence = NLicence + datetime.timedelta(days=-30)

    # variable avec le debut de la certif medical avec le format année/mois/jours
    Dcertif = "2021/05/18"                    # à remplacer par la donnée correspondante dans la bdd
    Dcertif = datetime.datetime.strptime(Dcertif, "%Y/%m/%d")
    # variable avec la fin de la certif medical avec le format année/mois/jours
    Fcertif = "2021/06/27"                                  # à remplacer par la donnée correspondante dans la bdd
    Fcertif = datetime.datetime.strptime(Fcertif, "%Y/%m/%d")

    # je met dans alerteCertif la date à partir de quand la notif doit apparaitre
    alerteCertif = Fcertif + datetime.timedelta(days=-14)



    #compteur de notification
    NB_NOTIF = 0

    #variable intermédiaire pour enclencher les notifictions et pouvoir integrer le compteur de notification
    compt = 0
    compt1 = 0
    compt2 = 0
    compt3 = 0

    #Variable pour ne plus afficher les notifications
    RenouLice = 0
    RenouCertif = 0

    # Variable que le tresorier met a une certaine valeur pour envoyer une notification
    NotifassuranceTresorier = 1  # à lier a un bouton sur la page gestion de membre du tresorier
    # Variable que le tresorier met a une certaine valeur pour envoyer une notification
    NotiflicenceTresorier = 1  # à lier a un bouton sur la page gestion de membre du tresorier

    # condition d'activation des notifications et compteur de notification
    if NotiflicenceTresorier == 1:
        NB_NOTIF = NB_NOTIF + 1
        compt = 1

    if NotifassuranceTresorier == 1:
        NB_NOTIF = NB_NOTIF + 1
        compt3 = 4

    if today > alerteLicence:
        NB_NOTIF = NB_NOTIF + 1
        compt1 = 2

    if today > alerteCertif:
        if today < Fcertif:
            NB_NOTIF = NB_NOTIF + 1
            compt2 = 3



    context = {
        "Fcertif": Fcertif,
        "NB_NOTIF": NB_NOTIF,
        "compt": compt,
        "compt1": compt1,
        "compt2": compt2,
        "compt3": compt3,
        "NotiflicenceTresorier": NotiflicenceTresorier,
        "NotifassuranceTresorier": NotifassuranceTresorier,
        "RenouLice" : RenouLice,
        "RenouCertif": RenouCertif,
    }

    return render(request, 'notif/notification.html', context)
