# Generated by Django 3.0.6 on 2020-05-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapStudentApp', '0022_auto_20200527_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumen',
            name='moduloGobNo',
            field=models.BigIntegerField(verbose_name='Módulo de Gobierno/Total No'),
        ),
        migrations.AlterField(
            model_name='resumen',
            name='moduloGobSi',
            field=models.BigIntegerField(verbose_name='Módulo de Gobierno/Total Si'),
        ),
    ]
