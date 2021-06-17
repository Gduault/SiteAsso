
from django.shortcuts import render
from datetime import datetime as date
import datetime


# Create your views here.
def notification(request):
    #Variable avec la date d'inscription de la licence
    DLicence = "2020/06/18"                                     # à remplacer par la donnée correspondante dans la bdd
    #Je dit que le format de la date sera année/mois/jours
    Dlicence = datetime.datetime.strptime(DLicence, "%Y/%m/%d")

    # Variable avec la date d'inscription de la licence +1 ans
    NLicence = Dlicence + datetime.timedelta(days=365)

    # je met dans today la date actuelle
    today = date.now()

    #je met dans alerteLicence la date à partir de quand la notif doit apparaitre
    alerteLicence = NLicence + datetime.timedelta(days=-30)

    #variable avec le debut de la certif medical avec le format année/mois/jours
    Dcertif = "2021/06/18"                                      # à remplacer par la donnée correspondante dans la bdd
    Dcertif = datetime.datetime.strptime(Dcertif, "%Y/%m/%d")
    # variable avec la fin de la certif medical avec le format année/mois/jours
    Fcertif = "2021/06/18"                                       # à remplacer par la donnée correspondante dans la bdd
    Fcertif = datetime.datetime.strptime(Fcertif, "%Y/%m/%d")

    #je met dans alerteCertif la date à partir de quand la notif doit apparaitre
    alerteCertif = Fcertif + datetime.timedelta(days=-14)

    #Variable que le tresorier met a une certaine valeur pour envoyer une notification
    NotifTresorier = 1                                          # à lier a un bouton sur la page gestion de memebre du tresorier

    context = {
        "Nlicence": NLicence,
        "alerteLicence": alerteLicence,
        "today": today,
        "Dcertif": Dcertif,
        "Fcertif": Fcertif,
        "alerteCertif": alerteCertif,
        "NotifTresorier": NotifTresorier,
        }


    return render(request, 'notif/notification.html', context)
