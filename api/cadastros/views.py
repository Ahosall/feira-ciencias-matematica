from rest_framework import viewsets
from .serializers import ProjetoSerializer
from .serializers import ParticipanteSerializer
from .serializers import EventoSerializer
from .serializers import ParticipanteProjetoSerializer
from .models import Projeto
from .models import ParticipanteProjeto
from .models import Participante
from .models import Evento


class ProjetoViewSet(viewsets.ModelViewSet):
    serializer_class = ProjetoSerializer
    queryset = Projeto.objects.all()


class ParticipanteViewSet(viewsets.ModelViewSet):
    serializer_class = ParticipanteSerializer
    queryset = Participante.objects.all()


class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()


class ParticipanteProjetoViewSet(viewsets.ModelViewSet):
    serializer_class = ParticipanteProjetoSerializer
    queryset = ParticipanteProjeto.objects.all()
