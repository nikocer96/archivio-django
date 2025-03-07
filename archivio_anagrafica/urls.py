from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path("", views.index),
    path('nuovo-utente/', views.CreaUtenteView.as_view(), name='crea_utente'),
    path('comuni/<int:provincia_id>/', views.ComuniPerProvinciaView.as_view(), name='comuni_per_provincia'),
    path('successo/', lambda request: HttpResponse('Utente creato con successo!'), name='successo'),
    path("utenti", views.ElencoUtenti.as_view(), name="utenti"),
    path("visualizza/<slug:slug>", views.DettagliUtente.as_view(), name="dettagli_utente"),
    path("utenti/rimuovi/<slug:slug>/", views.EliminaUtente.as_view(), name="rimuovi_utente")
]
