from django.contrib import admin
from .models import Contacto , Novedad

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Novedad)
class Admin(admin.ModelAdmin):
    pass
