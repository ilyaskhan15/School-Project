from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['user','name','department', 'office_location','hire_date']
    search_fields = ['department', 'user__first_name', 'user__last_name']
    
    
    def name(self, obj):
        return obj.user.get_full_name()
    name.short_description = "Teacher Name"

# Register your models here.
