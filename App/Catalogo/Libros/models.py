from django.db import models
from App.Catalogo.Categorias.models import Categoria

class Libro(models.Model):

    nombre = models.CharField(verbose_name='Nombre',max_length=100)
    costoactual = models.BigIntegerField(verbose_name='CostoActual', null=True, blank=True)
    existencia =models.BigIntegerField(verbose_name='Existencia', null=True, blank=True)
    categorias = models.ForeignKey(Categoria, verbose_name='Categorias', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Libros'

    def __str__(self):
        return f'{self.nombre}-{self.costoactual}-{self.existencia}'
