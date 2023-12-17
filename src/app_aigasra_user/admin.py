from django.contrib import admin
from .models import AigasraUser , UserFile

# Register your models here.
@admin.register(AigasraUser)
class AigasraUserAdmin(admin.ModelAdmin):
    pass

# Register your models here.
@admin.register(UserFile)
class UserFileAdmin(admin.ModelAdmin):
    pass
