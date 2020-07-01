from django.shortcuts import render,  redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import StudentInformation, Encuesta, Zona, Resumen, Incidencias
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models import F, Q, Sum
from django.db import IntegrityError
from .forms import IncidenciasForm
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
import json
from datetime import datetime


# Create your views here.


@login_required(login_url='/login/')
def profile(request):
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except:
        pass
    today = datetime.today()
    # activosCamaguey = StudentInformation.objects.filter(
    #     municipality='Camagüey').count()
    # totalEstudiantes = StudentInformation.objects.count()
    # coordenadas = StudentInformation.objects.filter(municipality='Camagüey').values_list(
    #     'name', 'address', 'carrera', 'phone', 'latitude', 'longitude')
    # allMap = StudentInformation.objects.exclude(
    #     latitude=None, longitude=None).count()
    allIncidencias = Incidencias.objects.count()
    totalEncuestas = Resumen.objects.aggregate(
        total_totalEnc=Sum('totalEnc')).values()
    totalZona = Zona.objects.filter(
        Q(startDate__year=today.year, startDate__month=today.month, startDate__day=today.day)).count()
    totalMapa = Resumen.objects.filter(
        Q(startDate__year=today.year, startDate__month=today.month, startDate__day=today.day))
    if totalMapa:
        totalMapa = Resumen.objects.filter(
            Q(startDate__year=today.year, startDate__month=today.month, startDate__day=today.day)).count()
    else:
        totalMapa = Resumen.objects.filter(
            Q(startDate__year=today.year, startDate__month=today.month, startDate__day=today.day-1)).count()

    coordenadas = Resumen.objects.filter(
        Q(startDate__year=today.year, startDate__month=today.month, startDate__day=today.day))
    if coordenadas:
        coordenadas = Resumen.objects.filter(Q(startDate__year=today.year, startDate__month=today.month, startDate__day=today.day)).values_list('zona__name', 'zona__latitude', 'zona__longitude', 'totalLifeYes', 'totalLifeNo', 'atetionYes',
                                                                                                                                                'atetionNo', 'mfYes', 'mfNo', 'servicesYes', 'servicesNo', 'safYes', 'safNo', 'alimentYes', 'alimentNo', 'moduloGobSi', 'moduloGobNo', 'startDate', 'totalEnc')
    else:
        coordenadas = Resumen.objects.filter(Q(startDate__year=today.year, startDate__month=today.month, startDate__day=today.day-1)).values_list('zona__name', 'zona__latitude', 'zona__longitude', 'totalLifeYes', 'totalLifeNo', 'atetionYes',
                                                                                                                                                  'atetionNo', 'mfYes', 'mfNo', 'servicesYes', 'servicesNo', 'safYes', 'safNo', 'alimentYes', 'alimentNo', 'moduloGobSi', 'moduloGobNo', 'startDate', 'totalEnc')

    return render(request, 'index.html', {'user': user, 'totalMapa': totalMapa, 'allIncidencias': allIncidencias, 'coordenadas': coordenadas, 'totalEncuestas': totalEncuestas, 'totalZona': totalZona})


@login_required(login_url='/login/')
def encuestaView(request):
    user = None
    okAddMensaje = ''
    errorAddMensaje = ''
    okResumenMensaje = ''
    errorResumenMensaje = ''
    try:
        user = User.objects.get(id=request.user.id)
    except ValidationError:
        pass
    # try:
    #     if not user.is_staff:
    #         return redirect("/noAutenticate/")
    # except ValidationError:
    #     pass
    today = datetime.today()
    allZone = Zona.objects.filter(
        startDate__year=today.year, startDate__month=today.month, startDate__day=today.day)
    if request.method == 'POST':
        if request.POST.get("form_type") == 'formOne':
            name = request.POST['name']
            zone = int(request.POST['zona'])
            syn = (request.POST['life'])
            life = True if syn == 'Si' else False
            synAtetion = (request.POST['atetion'])
            atetion = True if synAtetion == 'atetionSi' else False
            synMf = (request.POST['mf'])
            mf = True if synMf == 'mfSi' else False
            synServices = (request.POST['services'])
            services = True if synServices == 'servicesSi' else False
            synSaf = (request.POST['saf'])
            saf = True if synSaf == 'safSi' else False
            synAliment = (request.POST['aliment'])
            aliment = True if synAliment == 'alimentSi' else False
            synModuloGob = (request.POST['gobierno'])
            moduloGob = True if synModuloGob == 'gobiernoSi' else False
            zona = Zona.objects.get(id=zone)
            encuestalInf = Encuesta(
                name=name, zona=zona, life=life, atetion=atetion, mf=mf, services=services, saf=saf, aliment=aliment, moduloGob=moduloGob)
            try:
                encuestalInf.save()
                okAddMensaje = 'Se han recopilado los datos correctamente de la encuesta'
            except:
                errorAddMensaje = 'No se ha podido guardar la encuesta ya ese abuelito realizó la encuesta en esa Zona'
        elif request.POST.get("form_type") == 'formTwo':
            zoneResumen = int(request.POST['zonaResumen'])
            totalEnc = int(request.POST['totalEnc'])
            viveSi = int(request.POST['viveSi'])
            viveNo = int(request.POST['viveNo'])
            atetionSi = int(request.POST['atetionSi'])
            atetionNo = int(request.POST['atetionNo'])
            mfSi = int(request.POST['mfSi'])
            mfNo = int(request.POST['mfNo'])
            servicesSi = int(request.POST['servicesSi'])
            servicesNo = int(request.POST['servicesNo'])
            safSi = int(request.POST['safSi'])
            safNo = int(request.POST['safNo'])
            alimentSi = int(request.POST['alimentSi'])
            alimentNo = int(request.POST['alimentNo'])
            moduloGobSi = int(request.POST['gobiernoResumenSi'])
            moduloGobNo = int(request.POST['gobiernoResumenNo'])
            startDate = request.POST['dateResumen']
            zona = Zona.objects.get(
                Q(startDate__year=today.year, startDate__month=today.month, startDate__day=today.day, id=zoneResumen))
            try:
                resumen = Resumen.objects.get(zona=zona)
                resumen.totalLifeYes = F('totalLifeYes') + viveSi
                resumen.totalLifeNo = F('totalLifeNo') + viveNo
                resumen.atetionYes = F('atetionYes') + atetionSi
                resumen.atetionNo = F('atetionNo') + atetionNo
                resumen.mfYes = F('mfYes') + mfSi
                resumen.mfNo = F('mfNo') + mfNo
                resumen.servicesYes = F('servicesYes') + servicesSi
                resumen.servicesNo = F('servicesNo') + servicesNo
                resumen.safYes = F('safYes') + safSi
                resumen.safNo = F('safNo') + safNo
                resumen.alimentYes = F('alimentYes') + alimentSi
                resumen.alimentNo = F('alimentNo') + alimentNo
                resumen.moduloGobSi = F('moduloGobSi') + moduloGobSi
                resumen.moduloGobNo = F('moduloGobNo') + moduloGobNo
                resumen.totalEnc = F('totalEnc') + totalEnc
                resumen.save(update_fields=['totalLifeYes', 'totalLifeNo', 'atetionYes', 'atetionNo', 'mfYes',
                                            'mfNo', 'servicesYes', 'servicesNo', 'safYes', 'safNo', 'alimentYes', 'alimentNo', 'moduloGobSi', 'moduloGobNo', 'totalEnc'])
                okResumenMensaje = 'Se han actualizado los datos correctamente del resumen de la encuesta'
            except Resumen.DoesNotExist:
                Resumen.objects.create(zona=zona, totalLifeYes=viveSi, totalLifeNo=viveNo, atetionYes=atetionSi, atetionNo=atetionNo, mfYes=mfSi,
                                       mfNo=mfNo, servicesYes=servicesSi, servicesNo=servicesNo, safYes=safSi, safNo=safNo, alimentYes=alimentSi, alimentNo=alimentNo, moduloGobSi=moduloGobSi, moduloGobNo=moduloGobNo, totalEnc=totalEnc, startDate=startDate)
                errorResumenMensaje = 'Se han creado el primer resumen para esta zona en el dia de hoy'

    return render(request, 'encuesta.html', {'user': user, 'allZone': allZone, 'okAddMensaje': okAddMensaje, 'errorAddMensaje': errorAddMensaje, 'okResumenMensaje': okResumenMensaje, 'errorResumenMensaje': errorResumenMensaje})


@login_required(login_url='/login/')
def incidenciaView(request):
    okMensaje = ''
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except ValidationError:
        pass
    if request.method == 'POST':
        form = IncidenciasForm(request.POST)
        if form.is_valid():
            form.save()
            okMensaje = 'Se han registrados los datos correctamente'
            return redirect('/accounts/profile/AllIncidencia/')
    else:
        form = IncidenciasForm()

    return render(request, 'incidencia.html', {'user': user, 'form': form, 'okMensaje': okMensaje})


@login_required(login_url='/login/')
def incidenciaEditView(request, id):
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except ValidationError:
        pass
    incidencias = Incidencias.objects.get(id=id)
    form = IncidenciasForm(instance=incidencias)
    if request.method == "POST":
        form = IncidenciasForm(request.POST, instance=incidencias)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/accounts/profile/AllIncidencia/')

    return render(request, 'incidencia.html', {'user': user, 'form': form})


@login_required(login_url='/login/')
def incidenciaDeleteView(request, id):
    incidencias = Incidencias.objects.get(id=id)
    incidencias.delete()
    return redirect('/accounts/profile/AllIncidencia/')


@login_required(login_url='/login/')
def incidenciaViewAll(request):
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except ValidationError:
        pass
    allIncidencias = Incidencias.objects.all()
    paginator = Paginator(allIncidencias, 25)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'allIncidencias.html', {'user': user, 'page_obj': page_obj, 'allIncidencias': allIncidencias})


@login_required(login_url='/login/')
def search(request):
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except ValidationError:
        pass
    query = request.GET.get('q', '')
    allIncidencias = []
    parametros = None
    page_obj = None
    errors = []
    if request.method == 'GET':
        if not request.GET.get('q', ''):
            errors.append('Por favor llene el campo de busqueda.')
        if query:
            allIncidencias = Incidencias.objects.filter(
                Q(name__icontains=query) | Q(address__icontains=query))
            # return HttpResponse(json.dumps(list(incideAddress)), content_type='application/json'
            paginator = Paginator(allIncidencias, 25)
            page = request.GET.get('page')
            page_obj = paginator.get_page(page)
            parametros = request.GET.copy()
            if parametros.__contains__('page'):
                del parametros['page']

    return render(request, 'search.html', {'user': user, 'errors': errors, 'parametros': parametros, 'page_obj': page_obj, 'query': query, 'allIncidencias': allIncidencias})


@login_required(login_url='/login/')
def totalPorZona(request):
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except ValidationError:
        pass
    query = request.GET.get('zonaName', '')
    today = datetime.today()
    allZone = Zona.objects.filter(
        Q(startDate__year=today.year, startDate__month=today.month, startDate__day=today.day))
    if not allZone:
        allZone = Zona.objects.filter(
            Q(startDate__year=today.year, startDate__month=today.month, startDate__day=today.day-1))
    totalPorZona = Resumen.objects.filter(zona__name=query).aggregate(total_totalEnc=Sum('totalEnc'),
                                                                      total_totalLifeYes=Sum('totalLifeYes'), total_totalLifeNo=Sum('totalLifeNo'), total_atetionYes=Sum('atetionYes'), total_atetionNo=Sum('atetionNo'), total_mfYes=Sum('mfYes'), total_mfNo=Sum('mfNo'), total_servicesYes=Sum('servicesYes'), total_servicesNo=Sum('servicesNo'), total_safYes=Sum('safYes'), total_safNo=Sum('safNo'), total_alimentYes=Sum('alimentYes'), total_alimentNo=Sum('alimentNo'), total_moduloGobSi=Sum('moduloGobSi'), total_moduloGobNo=Sum('moduloGobNo'))
    return render(request, 'totalZona.html', {'query': query, 'user': user, 'totalPorZona': totalPorZona, 'allZone': allZone})


@login_required(login_url='/login/')
def mapPorZona(request):
    user = None
    totalEncuestas = None
    totalZona = None
    totalMapa = None
    allIncidencias = None
    coordenadas = None
    try:
        user = User.objects.get(id=request.user.id)
    except ValidationError:
        pass
    query = request.GET.get('dateZona', '')
    allDateZone = Zona.objects.distinct().values_list(
        'startDate', flat=True).order_by('startDate')
    if query:
        totalEncuestas = Resumen.objects.filter(startDate=query).aggregate(
            total_totalEnc=Sum('totalEnc')).values()
        totalZona = Zona.objects.filter(startDate=query).count()
        totalMapa = Resumen.objects.filter(startDate=query).count()
        allIncidencias = Incidencias.objects.filter(startDate=query).count()
        coordenadas = Resumen.objects.filter(startDate=query).values_list('zona__name', 'zona__latitude', 'zona__longitude', 'totalLifeYes', 'totalLifeNo', 'atetionYes',
                                                                          'atetionNo', 'mfYes', 'mfNo', 'servicesYes', 'servicesNo', 'safYes', 'safNo', 'alimentYes', 'alimentNo', 'moduloGobSi', 'moduloGobNo', 'startDate', 'totalEnc')
    return render(request, 'mapPorZona.html', {'coordenadas': coordenadas, 'allIncidencias': allIncidencias, 'totalMapa': totalMapa, 'totalZona': totalZona, 'totalEncuestas': totalEncuestas, 'query': query, 'user': user, 'totalPorZona': totalPorZona, 'allDateZone': allDateZone})


@login_required(login_url='/login/')
def totalesEncuestasZona(request):
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except ValidationError:
        pass
    total = Resumen.objects.aggregate(total_totalEnc=Sum('totalEnc'),
                                      total_totalLifeYes=Sum('totalLifeYes'), total_totalLifeNo=Sum('totalLifeNo'), total_atetionYes=Sum('atetionYes'), total_atetionNo=Sum('atetionNo'), total_mfYes=Sum('mfYes'), total_mfNo=Sum('mfNo'), total_servicesYes=Sum('servicesYes'), total_servicesNo=Sum('servicesNo'), total_safYes=Sum('safYes'), total_safNo=Sum('safNo'), total_alimentYes=Sum('alimentYes'), total_alimentNo=Sum('alimentNo'), total_moduloGobSi=Sum('moduloGobSi'), total_moduloGobNo=Sum('moduloGobNo')).values()
    zonaName = Resumen.objects.distinct().values_list(
        'zona__name', flat=True).order_by('zona__name')
    result = {}
    for dato in zonaName:
        totalEncuestaPorZona = Resumen.objects.filter(zona__name=dato).aggregate(total_totalEnc=Sum('totalEnc'),
                                                                                 total_totalLifeYes=Sum('totalLifeYes'), total_totalLifeNo=Sum('totalLifeNo'), total_atetionYes=Sum('atetionYes'), total_atetionNo=Sum('atetionNo'), total_mfYes=Sum('mfYes'), total_mfNo=Sum('mfNo'), total_servicesYes=Sum('servicesYes'), total_servicesNo=Sum('servicesNo'), total_safYes=Sum('safYes'), total_safNo=Sum('safNo'), total_alimentYes=Sum('alimentYes'), total_alimentNo=Sum('alimentNo'), total_moduloGobSi=Sum('moduloGobSi'), total_moduloGobNo=Sum('moduloGobNo')).values()
        result[dato] = totalEncuestaPorZona
    return render(request, 'totalesZona.html', {'total': total, 'result': result, 'user': user})


@login_required(login_url='/login/')
def zonaView(request):
    latitude = 0
    longitude = 0
    okMensaje = ''
    errorMensaje = ''
    user = None
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        raise 'Requested user not found.'
    if request.method == 'POST':
        name = request.POST['nameZona']
        coordinador = request.POST['coordeinadorZona']
        cantEstudLocal = int(request.POST['estLocal'])
        cantEstudParte = int(request.POST['estParte'])
        latitude = float(request.POST['latitud'])
        longitude = float(request.POST['longitud'])
        startDate = request.POST['dateZona']
        coordenadas = Zona.objects.filter(name=name).values_list(
            'latitude', 'longitude').first()
        if coordenadas:
            latitude = coordenadas[0]
            longitude = coordenadas[1]
        try:
            zonaAdd = Zona(name=name, coordinador=coordinador, cantEstudLocal=cantEstudLocal,
                           cantEstudParte=cantEstudParte, latitude=latitude, longitude=longitude, startDate=startDate)
            zonaAdd.save()
            if latitude == 0 or longitude == 0:
                okMensaje = 'Se añadio la zona sin coordenadas, adicione los datos que faltan en la parte administrativa del sistema. '
            else:
                okMensaje = 'Se añadio la zona al sistema correctamente. '
        except IntegrityError:
            errorMensaje = 'No puede añadir dos zonas con nombres iguales el mismo día. '

    return render(request, 'zonas.html', {'errorMensaje': errorMensaje, 'okMensaje': okMensaje, 'user': user, })
