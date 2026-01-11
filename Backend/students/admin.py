from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentUserModel(admin.ModelAdmin):
    list_display = ['user','name','class_level','degree_name','gpa','roll_no' ]
    search_fields = ['user__first_name', 'user__last_name', 'roll_no']
    list_display_links = ['user']
    
    def name(self, obj):
        return obj.user.get_full_name()
    name.short_description = "Student Name"
    

# Register your models here.
