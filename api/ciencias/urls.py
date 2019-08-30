from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CienciasProjetoViewSet
from .views import CienciasParticipanteViewSet

router = DefaultRouter()
router.register(r'projetos', CienciasProjetoViewSet)
router.register(r'participantes', CienciasParticipanteViewSet)

urlpatterns = [
    path("", include(router.urls))
]