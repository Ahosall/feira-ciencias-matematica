from django.contrib import admin
from .models import Projeto
from .models import Participante
from .models import Evento
from .models import ParticipanteProjeto
# Register your models here.

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'materia')

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

class ParticipanteProjetoInLine(admin.TabularInline):
    model = ParticipanteProjeto

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'projeto')
    inlines = [
       ParticipanteProjetoInLine
   ]
