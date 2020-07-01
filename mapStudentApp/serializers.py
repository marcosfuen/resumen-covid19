from rest_framework import serializers
from .models import Resumen, Zona, Incidencias


class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = ['name', 'coordinador',
                  'cantEstudLocal', 'cantEstudParte', 'latitude', 'longitude', 'startDate']


class ResumenSerializer(serializers.ModelSerializer):
    zona = ZonaSerializer()

    class Meta:
        model = Resumen
        fields = ['zona', 'totalLifeYes', 'totalLifeNo', 'atetionYes', 'atetionNo', 'mfYes',
                  'mfNo', 'servicesYes', 'servicesNo', 'safYes', 'safNo', 'alimentYes', 'alimentNo', 'moduloGobSi', 'moduloGobNo', 'totalEnc']


class IncidenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidencias
        fields = ['name', 'address', 'incidencia', 'isResolve', 'startDate']
