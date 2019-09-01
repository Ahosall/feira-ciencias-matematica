from django.db import models

# Create your models here.
class Projeto(models.Model):

    MATEMATICA='1'
    CIENCIAS='2'

    MATERIA = (
        (MATEMATICA, 'Matemática'),
        (CIENCIAS, 'Ciências')
    )


    QTDMAXMIN = (
        ('3','3'),
        ('4','4')
    )

    materia = models.IntegerField(choices=MATERIA)
    descricao = models.CharField(max_length=50)
    quantidade = models.IntegerField(choices=QTDMAXMIN)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural  = "Projetos"