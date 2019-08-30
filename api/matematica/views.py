from rest_framework import viewsets
from .serializers import ProjetoSerializer
from .serializers import ParticipanteSerializer
from .models import Projeto
from .models import Participante


class ProjetoViewSet(viewsets.ModelViewSet):
    serializer_class = ProjetoSerializer
    queryset = Projeto.objects.all()


class ParticipanteViewSet(viewsets.ModelViewSet):
    serializer_class = ParticipanteSerializer
    queryset = Participante.objects.all()
