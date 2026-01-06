from django.db import models
from django.conf import settings

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')
    employee_id = models.PositiveIntegerField(unique=True)
    department = models.CharField(max_length=255)
    hire_date = models.DateField()
    office_location = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'app_teachers'
    
    
    def __str__(self) -> str:
        return f"{self.user.get_full_name()} ({self.employee_id})"
    

# Create your models here.
