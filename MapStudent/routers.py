from rest_framework import routers
from mapStudentApp.viewsets import ResumenViewSet, IncidenciasViewSet


router = routers.DefaultRouter()


router.register(r'resumen', ResumenViewSet)
router.register(r'incidencias', IncidenciasViewSet)
