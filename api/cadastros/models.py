from django.db import models

# Create your models here.


class Projeto(models.Model):

    MATEMATICA = 1
    CIENCIAS = 2

    MATERIA = (
        (MATEMATICA, 'Matemática'),
        (CIENCIAS, 'Ciências')
    )

    QTDMAXMIN = (
        (3, '3'),
        (4, '4'),
	(5, '5')
    )

    materia = models.IntegerField(choices=MATERIA)
    descricao = models.CharField(max_length=50)
    quantidade = models.IntegerField(choices=QTDMAXMIN)

    def __str__(self):
        return f'[{self.get_materia_display()}] - {self.descricao}'

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"


class Participante(models.Model):

    SEXO = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )

    GRUPOS = (
        ('1', 'GRUPO - 1 - CIENCIAS'),
        ('2', 'GRUPO - 2 - CIENCIAS'),
        ('3', 'GRUPO - 3 - CIENCIAS'),
        ('4', 'GRUPO - 4 - CIENCIAS'),
        ('5', 'GRUPO - 1 - MATEMATICA'),
        ('6', 'GRUPO - 2 - MATEMATICA'),
        ('7', 'GRUPO - 3 - MATEMATICA')

    )
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=120)
    sexo = models.CharField(choices=SEXO, max_length=2)
    grupo = models.CharField(choices=GRUPOS, max_length=2)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"


class Evento(models.Model):
    descricao = models.CharField(max_length=100)
    projeto = models.ForeignKey(
        to='cadastros.Projeto', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def save(self, *args, **kwargs):
       super().save(*args, **kwargs)

       projetos = Projeto.objects.filter(pk=self.projeto_id).first()
       quantidade = projetos.quantidade
       for p in range(0, quantidade):
           ParticipanteProjeto.objects.update_or_create(evento=self,ordem=p+1)


class ParticipanteProjeto(models.Model):
    evento = models.ForeignKey(
        to='cadastros.Evento', 
        on_delete=models.CASCADE
        )
    ordem = models.IntegerField(default=0) 
    participante = models.ForeignKey(
        to='cadastros.Participante', 
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
        )

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = "Participante Projeto"
        verbose_name_plural = "Participantes Projetos"
