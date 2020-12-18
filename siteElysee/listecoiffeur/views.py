from django.shortcuts import render

# Create your views here.
from .models import Coiffeur


def liste_coiffeur(request):
    listecoiffeur = Coiffeur.objects.All()
    return render(request,'listecoiffeur/Header.html',{'listecoiffeurs':listecoiffeur})