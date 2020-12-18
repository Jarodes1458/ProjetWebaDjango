from django.shortcuts import render

# Create your views here.

def liste_coiffeur(request):
    return render(request,'listecoiffeur/Header.html')