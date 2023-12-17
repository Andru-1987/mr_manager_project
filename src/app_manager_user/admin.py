from django.contrib import admin
from .models import ManagerUser , UserFile

# Register your models here.
@admin.register(ManagerUser)
class ManagerUserAdmin(admin.ModelAdmin):
    pass

# Register your models here.
@admin.register(UserFile)
class UserFileAdmin(admin.ModelAdmin):
    pass
