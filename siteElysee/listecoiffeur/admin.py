from django.contrib import admin

# Register your models here.
from .models import Coiffeur, Tranchehoraire, RendezVous , Periode

admin.site.register(Coiffeur)
admin.site.register(Tranchehoraire)
admin.site.register(RendezVous)
admin.site.register(Periode)

