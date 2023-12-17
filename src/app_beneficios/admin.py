from django.contrib import admin
from .models import Curso,BibliotecaTecnica ,Normativa
# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    ...


@admin.register(Normativa)
class NormativaAdmin(admin.ModelAdmin):
    ...

@admin.register(BibliotecaTecnica)
class BibliotecaTecnicaAdmin(admin.ModelAdmin):
    ...
