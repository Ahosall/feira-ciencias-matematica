from rest_framework import viewsets
from .serializers import ProjetoSerializer
from .models import Projeto


class ProjetoViewSet(viewsets.ModelViewSet):
    serializer_class = ProjetoSerializer
    queryset = Projeto.objects.all()