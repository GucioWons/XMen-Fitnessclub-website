from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Account(models.Model):
    TYPE_CHOICES = [
        ('CLIENT', 'Client'),
        ('TRAINER', 'Trainer'),
        ('DIETICIAN', 'Dietician'),
        ('STAFF', 'Staff'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    pass_expire = models.DateField(null=True, blank=True)