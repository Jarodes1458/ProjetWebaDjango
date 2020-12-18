from django.urls import path
from . import views


urlpatterns = [
    path('', views.liste_coiffeur, name='liste_coiffeur'),
]