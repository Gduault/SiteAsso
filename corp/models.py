from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models


class Assurance_Complementaire(models.Model):
    NOM_ASSURANCE = models.CharField(max_length=100)
    DATE_REGLEMENT = models.DateTimeField()
    MODE_PAIEMENT = models.CharField(max_length=10)
    NB_CHEQUE = models.IntegerField()
    MONTANT = models.IntegerField()


class Certif_Medical(models.Model):
    D_DEBUT = models.DateField()
    D_FIN = models.DateField()


class Adherent(models.Model):
    ID_CERTIF = models.ForeignKey(Certif_Medical, on_delete=models.CASCADE)
    ID_ASSURANCE = models.ForeignKey(Assurance_Complementaire, on_delete=models.CASCADE)
    CIVILITE = models.CharField(max_length=30)
    NOM = models.CharField(max_length=30)
    PRENOM = models.CharField(max_length=30)
    PHOTO = models.ImageField()
    STATUS = models.CharField(max_length=30)
    LIEU_NAISSANCE = models.CharField(max_length=30)
    DATE_NAISSANCE = models.DateField()
    TEL_FIX = models.CharField(max_length=10)
    TEL_PORT = models.CharField(max_length=30)
    EMAIL = models.EmailField()
    ROLE_ADHERENT = models.CharField(max_length=30)
    REMARQUE = models.CharField(max_length=500)
    CLE_MOULIN = models.BooleanField(default=False)
    FONCTION = models.CharField(max_length=30)
    MBCA = models.BooleanField(default=False)
    NUM_LICENCE = models.CharField(max_length=20)
    TYPE_LICENCE = models.CharField(max_length=10)
    ASSURANCE_COMP = models.CharField(max_length=30)
    CLUB = models.CharField(max_length=30)
    DATE_INSCRIPTION = models.DateField()
    ADD_1 = models.CharField(max_length=30)
    ADD_2 = models.CharField(max_length=30)
    ADD_3 = models.CharField(max_length=30)
    CP = models.CharField(max_length=5)
    VILLE = models.CharField(max_length=30)
    PAYS = models.CharField(max_length=30)
    PER_CONTACT = models.CharField(max_length=30)
    NUM_PER_CONTACT = models.CharField(max_length=30)
    ALLERGIE = models.BooleanField()
    MDC_REF = models.CharField(max_length=30)
    NUM_TEL_MDC = models.CharField(max_length=10)
    DATE_RGL = models.DateTimeField()
    MODE_PAIEMENT = models.CharField(max_length=10)
    NB_CHEQUE = models.IntegerField()
    MONTANT = models.IntegerField()
    ADHESION = models.CharField(max_length=30)
    LICENCE = models.BooleanField(default=False)
    LOC_DETENTEUR = models.BooleanField()
    LOC_STAB = models.BooleanField()
    LOC_BLOC = models.BooleanField()


class Evenement(models.Model):
    H_DEBUT = models.DateTimeField()
    H_FIN = models.DateTimeField()
    NB_PERS_MAX = models.IntegerField()
    DATE = models.DateField()
    NB_PERS = models.IntegerField()
    ETAT_EVENEMENT = models.BooleanField(default=False)


class Type_Evenement(models.Model):
    ID_ADHERENT = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    ID_EVENEMENT = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    NOM_EVENEMENT = models.CharField(max_length=30)

class carousel(models.Model):
    image = models.ImageField(upload_to='static/img/')
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title