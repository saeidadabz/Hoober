from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    USER_TYPES = (
        ('normal', 'NormalUser'),
        ('consultant', 'Consultant'),
        ('employer', 'Employer'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='normal')

    phone_number = models.CharField(max_length=15, unique=True)