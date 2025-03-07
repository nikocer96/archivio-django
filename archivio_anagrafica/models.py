from django.db import models
from django.utils.text import slugify

# Create your models here.

class Provincia(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=2, unique=True)
    
    def __str__(self):
        return f"{self.nome}"


class Comune(models.Model):
    comune = models.CharField(max_length=100)
    pro_com_t = models.CharField(max_length=20, unique=True)
    provincia = models.ForeignKey(Provincia, related_name="comuni", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.comune}"
    

class Utente(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField(null=True)
    codice_fiscale = models.CharField(max_length=16, unique=True)
    provincia_nascita = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True, related_name="utenti_nati")
    comune_nascita = models.ForeignKey(Comune, on_delete=models.SET_NULL, null=True, related_name="utenti_nati")
    provincia_residenza = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True, related_name="utenti_residenti")
    comune_residenza = models.ForeignKey(Comune, on_delete=models.SET_NULL, null=True, related_name="utenti_residenti")
    slug = models.SlugField(null=True, blank=True, db_index=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nome} {self.cognome}"
    

class TitoloStudio(models.Model):
    nome = models.CharField(max_length=100)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name="titoli_studio")
    
    def __str__(self):
        return f"{self.nome}"

class Documento(models.Model):
    immagine = models.FileField(upload_to="immagini")
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name="documenti")
    
    def __str__(self):
        return f"{self.immagine}"
    
class RegistroUtente(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)