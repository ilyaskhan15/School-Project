from django.contrib import admin
from .models import ClassLevel, Section

@admin.register(ClassLevel)
class ClassLevelModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    
    
@admin.register(Section)
class SectionModelAdmin(admin.ModelAdmin):
    list_display = ['class_level', 'name']

# Register your models here.
