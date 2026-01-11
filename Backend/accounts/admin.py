from django.contrib import admin
from .models import User
from django.utils.html import format_html

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['profile_image_preview','email','get_full_name', 'email_verified', 'is_superuser']
    search_fields = ['first_name','last_name', 'email']
    list_display_links = ['email']
    
    
    def profile_image_preview(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" width="40", style="border-radius:50%;" />',
                obj.profile_image.url
            )
        return "-"
    profile_image_preview.short_description = "Profile Image"