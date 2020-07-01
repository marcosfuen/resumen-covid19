from rest_framework import viewsets, filters
from .serializers import ResumenSerializer, IncidenciasSerializer
from .models import Resumen, Incidencias
from django.db.models import Sum
from rest_framework.decorators import action
from rest_framework.response import Response


class ResumenViewSet(viewsets.ModelViewSet):
    '''
    Muestra el resumen de todas las encuestas.
    '''
    queryset = Resumen.objects.all()
    serializer_class = ResumenSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('zona__name', 'totalLifeYes', 'totalLifeNo', 'atetionYes', 'atetionNo', 'mfYes',
                     'mfNo', 'servicesYes', 'servicesNo', 'safYes', 'safNo', 'alimentYes', 'alimentNo', 'moduloGobSi', 'moduloGobNo')
    ordering_fields = ('id',)
    http_method_names = ['get', 'head']

    @action(detail=False, methods=['get'])
    def resumen_total_zonas(self, request):
        '''
        Muestra el total de encuestas por zona asi como total por preguntas Si y por preguntas No.
        '''
        zonaName = Resumen.objects.distinct().values_list(
            'zona__name', flat=True).order_by('zona__name')
        result = {}
        for dato in zonaName:
            result[dato] = self.filter_queryset(self.queryset).filter(zona__name=dato).aggregate(total_totalEnc=Sum('totalEnc'),
                                                                                                 total_totalLifeYes=Sum('totalLifeYes'), total_totalLifeNo=Sum('totalLifeNo'), total_atetionYes=Sum('atetionYes'), total_atetionNo=Sum('atetionNo'), total_mfYes=Sum('mfYes'), total_mfNo=Sum('mfNo'), total_servicesYes=Sum('servicesYes'), total_servicesNo=Sum('servicesNo'), total_safYes=Sum('safYes'), total_safNo=Sum('safNo'), total_alimentYes=Sum('alimentYes'), total_alimentNo=Sum('alimentNo'), total_moduloGobSi=Sum('moduloGobSi'), total_moduloGobNo=Sum('moduloGobNo'))
        self.queryset = result
        # Aplicar otros filtros del viewset
        queryset = self.filter_queryset(self.queryset)

        # Serializar resultados
        serializer = self.get_serializer(queryset, many=True)
        return Response(result)

    @action(detail=False, methods=['get'])
    def total(self, request):
        '''
        Muestra el total por encuesta, por pregunta Si y por pregunta No.
        '''
        zonaName = Resumen.objects.aggregate(total_totalEnc=Sum('totalEnc'),
                                             total_totalLifeYes=Sum('totalLifeYes'), total_totalLifeNo=Sum('totalLifeNo'), total_atetionYes=Sum('atetionYes'), total_atetionNo=Sum('atetionNo'), total_mfYes=Sum('mfYes'), total_mfNo=Sum('mfNo'), total_servicesYes=Sum('servicesYes'), total_servicesNo=Sum('servicesNo'), total_safYes=Sum('safYes'), total_safNo=Sum('safNo'), total_alimentYes=Sum('alimentYes'), total_alimentNo=Sum('alimentNo'), total_moduloGobSi=Sum('moduloGobSi'), total_moduloGobNo=Sum('moduloGobNo'))
        return Response(zonaName)


class IncidenciasViewSet(viewsets.ModelViewSet):
    '''
    Muestra todas la incidencias.
    '''
    queryset = Incidencias.objects.all()
    serializer_class = IncidenciasSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'latitude', 'longitude', 'isResolve', 'startDate')
    ordering_fields = ('id',)
    http_method_names = ['get', 'head']
