from django.contrib import admin
from . import models

class UserProfileAdminModel(admin.ModelAdmin):
    list_display = ('profile_image', 'full_name', 'email', 'is_superuser', 'email_verified')


admin.site.register(models.User, UserProfileAdminModel)
# Register your models here.
