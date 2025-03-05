import os
import django

# Imposta il DJANGO_SETTINGS_MODULE al tuo settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archivio.settings')
django.setup()

from archivio_anagrafica.models import Provincia, Comune
import csv

with open('data/comuni.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        provincia, created = Provincia.objects.get_or_create(
            nome=row['den_prov'],
            defaults={'sigla': row.get('sigla', '')}
        )
        Comune.objects.get_or_create(
            comune=row['comune'],
            pro_com_t=row['pro_com_t'],
            provincia=provincia
        )
