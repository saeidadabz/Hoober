from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    Roles = (
        ('normal', 'NormalUser'),
        ('consultant', 'Consultant'),
        ('employer', 'Employer'),
    )
    role = models.CharField(max_length=20, choices=Roles, default='normal')

    phone_number = models.CharField(max_length=15, unique=True, null=True)

    def __str__(self):
        return self.username