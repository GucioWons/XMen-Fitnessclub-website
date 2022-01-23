from django.contrib import admin

# Register your models here.
from Products.models import Pass, Diet, Training

admin.site.register(Pass)
admin.site.register(Diet)
admin.site.register(Training)