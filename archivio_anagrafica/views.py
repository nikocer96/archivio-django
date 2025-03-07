from django.shortcuts import render
from .models import Comune
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic import View, ListView, DetailView, DeleteView
from .models import Utente
from .form import UtenteForm
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, "archivio_anagrafica/index.html")

class ElencoUtenti(ListView):
    template_name = "archivio_anagrafica/elenco_utenti.html"
    model = Utente
    context_object_name = "utenti"

class CreaUtenteView(CreateView):
    model = Utente
    form_class = UtenteForm
    template_name = 'archivio_anagrafica/crea_utente.html'
    success_url = '/successo/'
        

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # Nascita
        provincia_nascita_id = self.request.GET.get('provincia_nascita') or self.request.POST.get('provincia_nascita')
        if provincia_nascita_id:
            form.fields['comune_nascita'].queryset = Comune.objects.filter(provincia_id=provincia_nascita_id)
        else:
            form.fields['comune_nascita'].queryset = Comune.objects.none()

        # Residenza
        provincia_residenza_id = self.request.GET.get('provincia_residenza') or self.request.POST.get('provincia_residenza')
        if provincia_residenza_id:
            form.fields['comune_residenza'].queryset = Comune.objects.filter(provincia_id=provincia_residenza_id)
        else:
            form.fields['comune_residenza'].queryset = Comune.objects.none()

        return form

# View per restituire i comuni di una provincia in formato JSON
class ComuniPerProvinciaView(View):
    def get(self, request, provincia_id):
        comuni = Comune.objects.filter(provincia_id=provincia_id).values('id', 'comune')
        return JsonResponse(list(comuni), safe=False)
    
class DettagliUtente(DetailView):
    template_name = "archivio_anagrafica/dettagli_utente.html"
    model = Utente
    context_object_name ="utente"
    
class EliminaUtente(DeleteView):
    template_name = "archivio_anagrafica/elenco_utenti.html"
    model = Utente
    context_object_name = "utente"
    success_url = reverse_lazy('utenti')