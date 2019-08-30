from rest_framework import serializers
from .models import Projeto
from .models import Participante


class ProjetoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projeto
        fields = ("id", "projeto", "quantidade_participantes")


class ParticipanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participante
        fields = ("id", "foto", "nome", "email", "telefone")
