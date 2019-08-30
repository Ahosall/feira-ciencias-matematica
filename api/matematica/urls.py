from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjetoViewSet
from .views import ParticipanteViewSet

router = DefaultRouter()
router.register(r'projetos', ProjetoViewSet)
router.register(r'participantes', ParticipanteViewSet)

urlpatterns = [
    path("", include(router.urls))
]