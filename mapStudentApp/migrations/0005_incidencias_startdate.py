# Generated by Django 3.0.6 on 2020-05-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapStudentApp', '0004_create_default_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidencias',
            name='startDate',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha del Reporte'),
        ),
    ]