from django.shortcuts import render
from .models import Realisation


def page_accueil_view(request):
    enregistrements = Realisation.objects.all()
    return render(request, 'realisations/index.html', {'realisations': enregistrements})