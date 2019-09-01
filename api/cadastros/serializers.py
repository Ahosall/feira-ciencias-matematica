from rest_framework import serializers
from .models import Projeto

class ProjetoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projeto
        fields = ("id", "materia", "descricao", "quantidade")