from django.contrib import admin

from App.Catalogo.Categorias.models import Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['id','nombre']