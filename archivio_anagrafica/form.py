from django import forms
from .models import RegistroUtente, Utente, Comune, Provincia
from django.contrib.auth.hashers import make_password

class RegistroUtenteForm(forms.ModelForm):
    class Meta:
        model = RegistroUtente
        fields = '__all__'
        widgets = {
            "password": forms.PasswordInput()
        }
        
class UtenteForm(forms.ModelForm):
    class Meta:
        model = Utente
        exclude = ['slug']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'border-1 border-black-500 w-full p-2'}),
            'cognome': forms.TextInput(attrs={'class': 'border-1 border-black-500 w-full p-2'}),
            'data_nascita': forms.TextInput(attrs={'class': 'border-1 border-black-500 w-full p-2'}),
            'codice_fiscale': forms.TextInput(attrs={'class': 'border-1 border-black-500 w-full p-2'}),
            'provincia_nascita': forms.Select(attrs={'class': 'border-1 border-black-500 w-full p-2'}),
            'comune_nascita': forms.Select(attrs={'class': 'border-1 border-black-500 w-full p-2'}),
            'provincia_residenza': forms.Select(attrs={'class': 'border-1 border-black-500 w-full p-2'}),
            'comune_residenza': forms.Select(attrs={'class': 'border-1 border-black-500 w-full p-2'}),
        }

    
