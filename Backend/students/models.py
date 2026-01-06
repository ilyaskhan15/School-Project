from django.db import models
from django.conf import settings

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    roll_no = models.PositiveIntegerField(unique=True)
    degree_name = models.CharField(max_length=255)
    enroll_date = models.DateField()
    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    credits = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    class_level = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'app_students'
        ordering = ['enroll_date']


    
    
    def __str__(self) -> str:
        return f"{self.user.get_full_name()} ({self.roll_no})"