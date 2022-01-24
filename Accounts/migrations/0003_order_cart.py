# Generated by Django 4.0.1 on 2022-01-24 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0002_diet_bought_training_bought'),
        ('Accounts', '0002_alter_account_pass_expire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('diets', models.ManyToManyField(blank=True, to='Products.Diet')),
                ('passs', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Products.pass')),
                ('trainings', models.ManyToManyField(blank=True, to='Products.Training')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diets', models.ManyToManyField(blank=True, to='Products.Diet')),
                ('passs', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Products.pass')),
                ('trainings', models.ManyToManyField(blank=True, to='Products.Training')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]