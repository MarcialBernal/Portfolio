from django.contrib import admin
from .models import Orders, OrdersLine

# Register your models here.

admin.site.register([Orders, OrdersLine])