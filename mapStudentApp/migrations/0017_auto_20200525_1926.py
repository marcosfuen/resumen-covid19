# Generated by Django 3.0.6 on 2020-05-25 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapStudentApp', '0016_auto_20200525_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumen',
            name='moduloGobNo',
            field=models.BigIntegerField(default=False, verbose_name='Modulo de Gobierno/Total No'),
        ),
        migrations.AddField(
            model_name='resumen',
            name='moduloGobSi',
            field=models.BigIntegerField(default=True, verbose_name='Modulo de Gobierno/Total Si'),
        ),
    ]
