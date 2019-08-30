from django.db import models

# Create your models here.
class Projeto(models.Model):
    PROJETOS = (
        ('Quadrilateros', 'Quadrilateros'),
        ('Quadrilateros', 'Quadrilateros'),
        ('Quadrilateros', 'Quadrilateros'),
        ('Quadrilateros', 'Quadrilateros')
    )
    QTD_PARTICIPANTES = (
        ('3', '3'),
        ('4', '4')
    )
    projeto = models.CharField(choices=PROJETOS, max_length=50)
    quantidade_participantes = models.CharField(
        choices=QTD_PARTICIPANTES, max_length=2)

    def __str__(self):
        return self.projeto

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"


class Participante(models.Model):
    foto = models.FileField()
    nome = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    telefone = models.CharField(max_length=12)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"
