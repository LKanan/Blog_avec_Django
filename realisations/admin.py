from django.contrib import admin
from .models import Realisation


# @admin.register(Realisation)
class RealisationAdmin(admin.ModelAdmin):
    # Alors on constate que pour modifier un enregistrement à partir de l'interface d'administration de django, il faut
    # appuyer sur le valeur dans la première colone, elle est sous forme d'un lien sur lequel on peut cliquer
    list_display = ('id', 'titre', 'description', 'image_url')


admin.site.register(Realisation, RealisationAdmin)