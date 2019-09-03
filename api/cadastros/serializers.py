from rest_framework import serializers
from .models import Projeto
from .models import Participante
from .models import Evento
from .models import ParticipanteProjeto

class ProjetoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projeto
        fields = ("id", "materia", "descricao", "quantidade")

class ParticipanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participante
        fields = ("id", "nome", "email", "sexo")

class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = ("id", "descricao", "projeto")

class ParticipanteProjetoSerializer(serializers.ModelSerializer):

    class Meta: 
        model = ParticipanteProjeto
        fields = ("id", "evento", "ordem", "participante")