from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Django already provides:
    # id (BigAutoField)
    # username
    # password (hashed)
    # last_login
    # is_active
    # is_staff
    # is_superuser
    # date_joined

    email = models.EmailField(unique=True,db_index=True,verbose_name="email address")
    email_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20,unique=True,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    profile_image = models.ImageField(upload_to="/profileImages/users",null=True,blank=True)

    class Meta:
        db_table = "app_users"
        ordering = ["-date_joined"]

    def __str__(self):
        return self.email

