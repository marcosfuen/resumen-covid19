from django.contrib import admin
from .models import StudentInformation, Encuesta, Zona, Resumen, Incidencias
# Register your models here.


class StudentInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'zona', 'address',
                    'carrera', 'yearStudent', 'phone')
    search_fields = ['name', 'zona__name', 'address',
                     'carrera', 'yearStudent', 'phone']


class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('name', 'zona', 'life', 'atetion',
                    'mf', 'services', 'saf', 'aliment', 'moduloGob', 'startDate')
    search_fields = ['name', 'zona__name', 'life', 'atetion',
                     'mf', 'services', 'saf', 'aliment', 'moduloGob', 'startDate']


class ZonaAdmin(admin.ModelAdmin):
    list_display = ('name', 'coordinador',
                    'cantEstudLocal', 'cantEstudParte', 'latitude', 'longitude', 'startDate')
    search_fields = ['name', 'coordinador',
                     'cantEstudLocal', 'cantEstudParte', 'latitude', 'longitude', 'startDate']


class ResumenAdmin(admin.ModelAdmin):
    list_display = ('zona', 'totalLifeYes', 'totalLifeNo', 'atetionYes',
                    'atetionNo', 'mfYes', 'mfNo', 'servicesYes', 'servicesNo', 'safYes', 'safNo', 'alimentYes', 'alimentNo', 'moduloGobSi', 'moduloGobNo', 'totalEnc', 'startDate')
    search_fields = ['zona__name', 'totalLifeYes', 'totalLifeNo', 'atetionYes',
                     'atetionNo', 'mfYes', 'mfNo', 'servicesYes', 'servicesNo', 'safYes', 'safNo', 'alimentYes', 'alimentNo', 'moduloGobSi', 'moduloGobNo', 'totalEnc', 'startDate']


class IncidenciasAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'incidencia', 'isResolve', 'startDate')
    search_fields = ['name', 'address', 'incidencia', 'isResolve', 'startDate']


admin.site.register(StudentInformation, StudentInformationAdmin)
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(Resumen, ResumenAdmin)
admin.site.register(Incidencias, IncidenciasAdmin)

admin.site.site_header = 'Encuesta COVID-19 - Administración'
admin.site.site_title = 'Sistema para Encuesta COVID-19 - Administración'
