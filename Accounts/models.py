from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from Products.models import Pass, Diet, Training


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

    def get_trainer_absolute_url(self):
        return reverse('accounts:trainer-view', kwargs={'my_id': self.id})
    def get_dietician_absolute_url(self):
        return reverse('accounts:dietician-view', kwargs={'my_id': self.id})

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    passs = models.ForeignKey(Pass, null=True, on_delete=models.CASCADE)
    diets = models.ManyToManyField(Diet, blank=True)
    trainings = models.ManyToManyField(Training, blank=True)

class Order(models.Model):
    username = models.CharField(max_length=50)
    passs = models.ForeignKey(Pass, null=True, on_delete=models.CASCADE)
    diets = models.ManyToManyField(Diet, blank=True)
    trainings = models.ManyToManyField(Training, blank=True)
    cost = models.DecimalField(decimal_places=2, max_digits=5)
    date = models.DateTimeField(default=timezone.now)