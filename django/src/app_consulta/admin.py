from django.contrib import admin
from .models import Consulta , ArchivoConsulta
# Register your models here.

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    ...

@admin.register(ArchivoConsulta)
class ArchivoConsultaAdmin(admin.ModelAdmin):
    ...

