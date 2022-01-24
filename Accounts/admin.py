from django.contrib import admin

# Register your models here.
from Accounts.models import Account, Cart, Order

admin.site.register(Account)
admin.site.register(Cart)
admin.site.register(Order)