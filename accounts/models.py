from django.contrib.auth.models import AbstractUser
from django.db import models
import re
from django.core.exceptions import ValidationError

# Create your models here.
def validate_phone(value):
    if not re.fullmatch(r'^[6-9]\d{9}$', value):
        raise ValidationError("Enter a valid 10-digit Indian phone number.")
    
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    )
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='student')

    phone = models.CharField(
        max_length=10,
        validators=[validate_phone],
        blank=True,
        null=True
    )