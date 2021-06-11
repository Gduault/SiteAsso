from corp.models import Adherent

class CustomUserForm(RegistrationForm):
    """
    Formulaire d'enregistrement personnalisé.
    """
    class Meta:
        # utilisation de notre modèle
        model = Adherent
        # ajout des champs nom, prenom et email.
        # Le champ password est ajouté automatiquement par la classe parente
        fields = ["nom", "prenom", "email"]