# Generated by Django 5.1.5 on 2025-03-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivio_anagrafica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utente',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
