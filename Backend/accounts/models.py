from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True,db_index=True,verbose_name="email address")
    email_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20,unique=True,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    profile_image = models.ImageField(upload_to="profileImages/users",null=True,blank=True)
    # Django already provides:
    # id (BigAutoField)
    # username
    # password (hashed)
    # last_login
    # is_active
    # is_staff
    # is_superuser
    # date_joined
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta:
        db_table = "app_users"
        ordering = ["-date_joined"]

    def __str__(self):
        return self.email or self.username