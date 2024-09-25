from django.db import models

from App.Catalogo.TipoEntrada.models import TipoEntrada

class Entrada(models.Model):
    fechaentrada = models.CharField(verbose_name='FechaEntrada', max_length=100)

    tipoentrada  = models.ForeignKey(TipoEntrada, verbose_name='TipoEntrada', on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'TiposEntradas'

    def __str__(self):
        return f'{self.fechaentrada}'

# Create your models here.
