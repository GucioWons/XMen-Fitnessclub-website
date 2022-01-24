from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from Products.validators import validate_file_extension


class Pass(models.Model):
    duration = models.IntegerField(unique=True)
    cost = models.DecimalField(decimal_places=2, max_digits=5)

    def get_add_to_cart_url(self):
        return reverse('products:add-pass-to-cart-view', kwargs={'my_id': self.id})

    def get_remove_from_cart_url(self):
        return reverse('products:remove-pass-from-cart-view', kwargs={'my_id': self.id})

class Training(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    file = models.FileField(upload_to='trainings', validators=[validate_file_extension])
    cost = models.DecimalField(decimal_places=2, max_digits=5)
    bought = models.ManyToManyField(User, related_name='bought_training', blank=True)

    def get_add_to_cart_url(self):
        return reverse('products:add-training-to-cart-view', kwargs={'my_id': self.id})

    def get_remove_from_cart_url(self):
        return reverse('products:remove-training-from-cart-view', kwargs={'my_id': self.id})

class Diet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    file = models.FileField(upload_to='diets', validators=[validate_file_extension])
    cost = models.DecimalField(decimal_places=2, max_digits=5)
    bought = models.ManyToManyField(User, related_name='bought_diet', blank=True)

    def get_add_to_cart_url(self):
        return reverse('products:add-diet-to-cart-view', kwargs={'my_id': self.id})

    def get_remove_from_cart_url(self):
        return reverse('products:remove-diet-from-cart-view', kwargs={'my_id': self.id})