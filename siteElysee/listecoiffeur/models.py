from django.db import models

# Create your models here.

class Coiffeur(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    numtel = models.CharField(max_length=200)
    poste = models.CharField(max_length=10)

class Tranchehoraire(models.Model):
    coiffeur = models.ForeignKey(Coiffeur,on_delete=models.CASCADE)
    tra_jour = models.CharField(max_length=100)
    tra_heure_debut_matin = models.DateTimeField
    tra_heure_fin_matin = models.DateTimeField
    tra_heure_debut_aprem = models.DateTimeField
    tra_heure_fin_aprem = models.DateTimeField

class RendezVous(models.Model)




