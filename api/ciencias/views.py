from rest_framework import viewsets
from .serializers import CienciasProjetoSerializer
from .serializers import CienciasParticipanteSerializer
from .models import CienciasProjeto
from .models import CienciasParticipante


class CienciasProjetoViewSet(viewsets.ModelViewSet):
    serializer_class = CienciasProjetoSerializer
    queryset = CienciasProjeto.objects.all()


class CienciasParticipanteViewSet(viewsets.ModelViewSet):
    serializer_class = CienciasParticipanteSerializer
    queryset = CienciasParticipante.objects.all()
