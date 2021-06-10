from django.contrib import admin
# Register your models here.

from corp.models import Adherent, Certif_Medical, Assurance_Complementaire, Evenement, Type_Evenement

admin.site.register(Adherent)
admin.site.register(Certif_Medical)
admin.site.register(Assurance_Complementaire)
admin.site.register(Evenement)
admin.site.register(Type_Evenement)


