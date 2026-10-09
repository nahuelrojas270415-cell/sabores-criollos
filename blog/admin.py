from django.contrib import admin
from .models import Receta

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'fecha')
    list_filter = ('categoria',)