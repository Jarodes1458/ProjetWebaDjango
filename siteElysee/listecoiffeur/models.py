from django.db import models
from django.conf import settings

# Create your models here.

class Coiffeur(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    numtel = models.CharField(max_length=200)
    poste = models.CharField(max_length=10)

class Tranchehoraire(models.Model):
    coiffeur = models.ForeignKey(Coiffeur,on_delete=models.CASCADE)
    jour = models.CharField(max_length=100)
    heure_debut_matin = models.DateTimeField()
    heure_fin_matin = models.DateTimeField()
    heure_debut_aprem = models.DateTimeField()
    heure_fin_aprem = models.DateTimeField()

class Periode(models.Model):
    date = models.DateField()
    heure_debut = models.DateTimeField()
    heure_fin = models.DateTimeField()

class RendezVous(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coiffeur = models.ForeignKey(Coiffeur,on_delete=models.CASCADE)
    rdv_prix = models.SmallIntegerField()
    rdv_statut = models.BooleanField()
    periodes = models.ManyToManyField(Periode)











