from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, null=True, blank=True)
    # Self-reference for hierarchy [cite: 27]
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('USER', 'Standard User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER')
    # Every user must belong to a company for isolation [cite: 28, 30]
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users', null=True)