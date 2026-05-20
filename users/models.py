from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    email_verified = models.BooleanField(default=False)

