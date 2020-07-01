from django.db import models
from django.utils import timezone

# Create your models here.


class Zona(models.Model):
    name = models.CharField('Nombre Zona', max_length=150)
    coordinador = models.CharField(
        'Nombre(s) y Apellido(s) del coordinador', max_length=150, blank=True, null=True)
    cantEstudLocal = models.BigIntegerField(
        'Cant. Estudiantes localizados', default=0, blank=True, null=True)
    cantEstudParte = models.BigIntegerField(
        'Cant. Estudiantes que dieron parte', default=0, blank=True, null=True)
    latitude = models.FloatField('Latitud', blank=True, null=True)
    longitude = models.FloatField('Longitud', blank=True, null=True)
    startDate = models.DateField('Fecha', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'zona_information'
        ordering = ['id']
        verbose_name = 'Información de la Zona'
        verbose_name_plural = 'Información de las Zonas'
        unique_together = [['name', 'startDate']]


class StudentInformation(models.Model):
    name = models.CharField('Nombre y Apellidos', max_length=150)
    zona = models.ForeignKey(
        Zona, verbose_name='zona', on_delete=models.CASCADE, default=None)
    address = models.CharField(
        'Dirección', max_length=150, blank=True, null=True)
    carrera = models.CharField(
        'Carrera', max_length=150, blank=True, null=True)
    yearStudent = models.CharField(
        'Año de estudio', max_length=300, blank=True, null=True)
    phone = models.CharField('Teléfono', max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student_information'
        ordering = ['id']
        verbose_name = 'Información del Estudiante'
        verbose_name_plural = 'Información de los Estudiantes'


class Encuesta(models.Model):
    name = models.CharField('Nombre y Apellidos', max_length=150)
    zona = models.ForeignKey(
        Zona, verbose_name='zona', on_delete=models.CASCADE, default=None)
    life = models.BooleanField('Vive solo', default=True)
    atetion = models.BooleanField(
        'Recibe atención de su familia', default=True)
    mf = models.BooleanField(
        'Recibe atención del médico de familia', default=True)
    services = models.BooleanField(
        'Tiene Usted servicio de mensajería para obtener los medicamentos', default=True)
    saf = models.BooleanField(
        'Recibe atención del SAF para obtener los alimentos', default=True)
    aliment = models.BooleanField(
        'Tiene Usted servicio de mensajería para obtener los alimentos', default=True)
    moduloGob = models.BooleanField(
        'Recibe Usted el modulo asignado por el gobierno', default=True)
    startDate = models.DateField(
        'Fecha', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'encuesta_information'
        ordering = ['id']
        verbose_name = 'Información del encuesta'
        verbose_name_plural = 'Información de las encuestas'


class Resumen(models.Model):
    zona = models.ForeignKey(
        Zona, verbose_name='zona', on_delete=models.CASCADE, default=None)
    totalLifeYes = models.BigIntegerField('Vive Solo/Total Si')
    totalLifeNo = models.BigIntegerField('Vive Solo/Total No')
    atetionYes = models.BigIntegerField('Atención de Familia/Total Si')
    atetionNo = models.BigIntegerField('Atención de Familia/Total No')
    mfYes = models.BigIntegerField('Médico de familia/Total Si')
    mfNo = models.BigIntegerField('Médico de familia/Total No')
    servicesYes = models.BigIntegerField(
        'Mensajería para medicamentos/Total Si')
    servicesNo = models.BigIntegerField(
        'Mensajería para medicamentos/Total No')
    safYes = models.BigIntegerField('SAF/Total Si')
    safNo = models.BigIntegerField('SAF/Total No')
    alimentYes = models.BigIntegerField('Mensajería para alimentos/Total Si')
    alimentNo = models.BigIntegerField('Mensajería para alimentos/Total No')
    moduloGobSi = models.BigIntegerField(
        'Módulo de Gobierno/Total Si',)
    moduloGobNo = models.BigIntegerField(
        'Módulo de Gobierno/Total No',)
    totalEnc = models.BigIntegerField(
        'Cant. de adultos mayores visitados', default=0)
    startDate = models.DateField('Fecha', default=timezone.now)

    def __str__(self):
        return self.zona.name

    class Meta:
        db_table = 'resumen_information'
        ordering = ['id']
        verbose_name = 'Resumen'
        verbose_name_plural = 'Resumenes'


class Incidencias(models.Model):
    name = models.CharField('Nombre y Apellidos', max_length=150)
    address = models.TextField('Dirección', max_length=250)
    incidencia = models.TextField('Incidencias', max_length=500)
    isResolve = models.BooleanField('Resuelta', default=False)
    startDate = models.DateField('Fecha del Reporte', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'incidencias_information'
        ordering = ['id']
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'
