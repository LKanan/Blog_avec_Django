# Generated by Django 4.2.4 on 2023-11-03 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realisations', '0002_rename_mesrealisations_mesrealisation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MesRealisation',
            new_name='Realisation',
        ),
    ]
