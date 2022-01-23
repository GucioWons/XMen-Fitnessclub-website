# Generated by Django 4.0.1 on 2022-01-23 21:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='bought',
            field=models.ManyToManyField(blank=True, related_name='bought_diet', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='training',
            name='bought',
            field=models.ManyToManyField(blank=True, related_name='bought_training', to=settings.AUTH_USER_MODEL),
        ),
    ]
