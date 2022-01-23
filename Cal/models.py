from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Class(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    max = models.IntegerField()
    date = models.DateTimeField()
    signed = models.ManyToManyField(User, related_name='signed_users', blank=True)

    def __str__(self):
        return (self.title + str(self.date))

    def get_absolute_url(self):
        return reverse('cal:class-view', kwargs={'my_id': self.id})

    def get_join_url(self):
        return reverse('cal:join-view', kwargs={'my_id': self.id})

    def get_leave_url(self):
        return reverse('cal:leave-view', kwargs={'my_id': self.id})