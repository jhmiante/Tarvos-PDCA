from django.db import models

from usuario.models import CustomUser


class PDCA(models.Model):
    usuario = models.ForeignKey(CustomUser, verbose_name='Usuário', on_delete=models.CASCADE)
    objetivo = models.CharField('Objetivo', max_length=200)
    data = models.DateField('Data')
    inicio = models.DateField('Inicio')
    fim = models.DateField('Fim')
    quem = models.CharField('Objetivo', max_length=100)
    descricao = models.TextField('Descrição', max_length=400)
    finalizado = models.BooleanField('Finalizado', default=False)

    def __str__(self):
        return f'PDCA: {self.objetivo}'

    def finalizar(self):
        self.finalizado = True


class PDCAItem(models.Model):
    pdca = models.ForeignKey(PDCA, verbose_name='PDCA', on_delete=models.CASCADE)
    data = models.DateField('Data')
    descricao = models.TextField('Descrição', max_length=400)

    def __str__(self):
        return f'{self.pdca} - {self.data}'
