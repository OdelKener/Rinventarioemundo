from django.db import models


from App.Catalogo.Entrada.models import Entrada
from App.Catalogo.Libros.models import Libro


class DetalleEntrada(models.Model):


 costoactual = models.BigIntegerField(verbose_name='CostoActual', null=True, blank=True)
 cantidad= models.BigIntegerField(verbose_name='Cantidad', null=True, blank=True)
 entrada = models.ForeignKey(Entrada, verbose_name='Entrada', on_delete=models.PROTECT)
 libro = models.ForeignKey(Libro, verbose_name='Libro', on_delete=models.PROTECT)


class Meta:
    verbose_name = 'DetallesEntradas'


def __str__(self):
    return f'{self.costoactual}-{self.cantidad}'

# Create your models here.
