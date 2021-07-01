from django.db import models


from django.db import models
# Creation de la classe Assurance_Complementaire qui permetra a l'utilisateur de renseigner plusieurs champ
# Tel que le nom de l'assurance, la date du reglement, avec quel mode de paiement, le nombre de cheque il fallu pour
# Payer et le montant


class Assurance_Complementaire(models.Model):
    # champ de caractere et qui peut contenir 30 caractere
    NOM_ASSURANCE = models.CharField(max_length=30)
    # La date du reglement a un format Date
    DATE_REGLEMENT = models.DateTimeField()
    # Le mode paiement 2 valeurs sera possible VIR pour le virement et CHQ pour les cheques
    MODE_PAIEMENT = models.CharField(max_length=3)
    # Le nombre de cheque sera en INT, attention si le mode de paiement est un VIREMENT, il n'y a pas de nombre de
    # cheque
    NB_CHEQUE = models.IntegerField()
    # Le montant sera le montant total pour payer l'assurance complementaire
    MONTANT = models.IntegerField()
    # Mise en place du modèle en abstract pour pouvoir le réutilisé des les autres applications


# Creation de la classe Certif_Medical qui contiendra la date de debut et de fin du certificat medical

class Certif_Medical(models.Model):
    # La date de debut est le debut du certificat medical, il pourra alors commencer les plongees
    D_DEBUT = models.DateField()
    # La date de fin est la fin du certificat medical, si elle est depasser il faudra le mettre a jour
    D_FIN = models.DateField()
    # Mise en place du modèle en abstract pour pouvoir le réutilisé des les autres applications


# Creation de la classe Adherent qui contiendra plusieurs informations personnel sur l'adherent tel que sont nom,
# son prenom, sa date de naissance et le lieu, ou il habite, son telephone etc

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
    # Le telephone de l'adherent,  sera de type char et pourra contenir 10 caracteres
    TEL_FIX = models.CharField(max_length=10)
    # Le telephone de l'adherent,  sera de type char et pourra contenir 10 caracteres
    TEL_PORT = models.CharField(max_length=10)
    EMAIL = models.EmailField()
    # Il y a plusieurs roles, membre, tresorier, directeur de plonge, president
    ROLE_ADHERENT = models.CharField(max_length=30)
    # Les remarques sera de type char avec une longeur de 500 afin que les adherents puissent mettre ce qu'ils veulent
    REMARQUE = models.CharField(max_length=500)
    # Par default il ne possede pas la cle = False sinon si il possede la cle = True
    CLE_MOULIN = models.BooleanField(default=False)
    # Un adherent peut avoir different fonction tel que responsable compresseur, ou materiel, technique etcc
    FONCTION = models.CharField(max_length=30)
    # Membre du conseil administratif
    MBCA = models.BooleanField(default=False)
    # Le numero de licence est de type char car il peut contenir des numeros et des lettres
    NUM_LICENCE = models.CharField(max_length=20)
    # Le type de licence peut avoir 2 valeurs soit Adulte ou Jeune
    TYPE_LICENCE = models.CharField(max_length=10)
    # Un adherent peuvent faire parti de different club de plongee comme GISSACG, ENTENTE SPORTIVE RENAULT, ....
    CLUB = models.CharField(max_length=30)
    # La date d'inscription sera la date sur le site
    DATE_INSCRIPTION = models.DateField()
    # L'adresse postale sera de type char avec une longueur max de 30 caracteres
    ADD_1 = models.CharField(max_length=30)
    # L'adresse postale sera de type char avec une longueur max de 30 caracteres
    ADD_2 = models.CharField(max_length=30)
    # L'adresse postale sera de type char avec une longueur max de 30 caracteres
    ADD_3 = models.CharField(max_length=30)
    # Le code postale sera de type char avec une longueur max de 5 caracteres
    CP = models.CharField(max_length=5)
    # La ville sera de type char avec une longueur max de 30 caracteres
    VILLE = models.CharField(max_length=30)
    # Le pays sera de type char avec une longueur max de 30 caracteres
    PAYS = models.CharField(max_length=30)
    # Sera le nom de la personne a contacter en cas de problemes
    PER_CONTACT = models.CharField(max_length=30)
    # Sera le numero de la personne a contacter en cas de problemes
    NUM_PER_CONTACT = models.CharField(max_length=30)
    # Allergie ne possede pas de valeur par defaut, il peut etre True ou False
    ALLERGIE = models.BooleanField()
    # Le nom du medecin referent
    MDC_REF = models.CharField(max_length=30)
    # Le numero du medecin referent
    NUM_TEL_MDC = models.CharField(max_length=10)
    # La date ou il a paye sa licence
    DATE_RGL = models.DateTimeField()
    # Le mode de paiement qui lui a permit de payer sa licence
    MODE_PAIEMENT = models.CharField(max_length=10)
    # Le nombre de cheque sera en INT, attention si le mode de paiement est un VIREMENT, il n'y a pas de nombre de
    # cheque
    NB_CHEQUE = models.IntegerField()
    # Le montant sera le montant total pour payer sa licence
    MONTANT = models.IntegerField()
    # Soit l'adherent est inscrit ou non inscrit ou membre passager
    ADHESION = models.CharField(max_length=30)
    # Il est false de base, si il paye sa licence = True
    LICENCE = models.BooleanField(default=False)
    # Soit il a loue un detenteur = True sinon = False
    LOC_DETENTEUR = models.BooleanField()
    # Soit il a loue un STAB = True sinon = False
    LOC_STAB = models.BooleanField()
    # Soit il a loue un BLOC = True sinon = False
    LOC_BLOC = models.BooleanField()
    # Mise en place du modèle en abstract pour pouvoir le réutilisé des les autres applications


class Evenement(models.Model):
    H_DEBUT = models.DateTimeField()
    H_FIN = models.DateTimeField()
    NB_PERS_MAX = models.IntegerField()
    DATE = models.DateField()
    NB_PERS = models.IntegerField()
    ETAT_EVENEMENT = models.BooleanField(default=False)
    # Mise en place du modèle en abstract pour pouvoir le réutilisé des les autres applications



class Type_Evenement(models.Model):
    ID_ADHERENT = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    ID_EVENEMENT = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    NOM_EVENEMENT = models.CharField(max_length=30)
    # Mise en place du modèle en abstract pour pouvoir le réutilisé des les autres applications

