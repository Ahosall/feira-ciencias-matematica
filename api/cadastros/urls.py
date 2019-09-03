from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjetoViewSet
from .views import ParticipanteViewSet
from .views import EventoViewSet
from .views import ParticipanteProjetoViewSet

router = DefaultRouter()
router.register(r'projetos', ProjetoViewSet)
router.register(r'participantes', ParticipanteViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'participantes-projetos', ParticipanteProjetoViewSet)

urlpatterns = [
    path("", include(router.urls))
]