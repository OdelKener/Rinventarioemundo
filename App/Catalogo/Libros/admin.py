from django.contrib import admin

from App.Catalogo.Libros.models import Libro
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre','categorias']
    list_display = ['id','nombre','costoactual','existencia','categorias']