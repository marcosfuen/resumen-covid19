from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

from mapStudentApp import views

app_name = 'mapStudentApp'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/profile/', views.profile, name='accountsProfile'),
    path('accounts/profile/encuesta/', views.encuestaView, name='encuesta'),
    path('accounts/profile/newZona/', views.zonaView, name='zona'),
    path('accounts/profile/newIncidencia/',
         views.incidenciaView, name='incidencia'),
    path('accounts/profile/AllIncidencia/',
         views.incidenciaViewAll, name='allIncidencia'),
    path('accounts/profile/editIncidencia/<int:id>',
         views.incidenciaEditView, name='editIncidencia'),
    path('accounts/profile/deleteIncidencia/<int:id>',
         views.incidenciaDeleteView, name='deleteIncidencia'),
    path('accounts/profile/search/', views.search, name='busquedaIncidencias'),
    path('accounts/profile/totalZona/', views.totalPorZona, name='totalPorZona'),
    path('accounts/profile/mapPorZona/', views.mapPorZona, name='mapPorZona'),
    path('accounts/profile/totalesEncuestasZona/',
         views.totalesEncuestasZona, name='totalesEncuestasZona'),
    # path('noAutenticate/', views.noAutenticate, name='noAutenticate'),
    # path('noPermission/', views.okSignupNoPermission, name='noPermission'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
