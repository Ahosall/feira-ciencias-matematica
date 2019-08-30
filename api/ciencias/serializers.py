from rest_framework import serializers
from .models import CienciasProjeto
from .models import CienciasParticipante


class CienciasProjetoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CienciasProjeto
        fields = ("id", "projeto", "quantidade_participantes")


class CienciasParticipanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CienciasParticipante
        fields = ("id", "foto", "nome", "email", "telefone")
