from django.contrib import admin
from .models import Cuota
# Register your models here.
@admin.register(Cuota)
class CuotaAdmin(admin.ModelAdmin):
    ...

