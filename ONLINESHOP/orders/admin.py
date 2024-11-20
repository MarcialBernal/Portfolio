from django.contrib import admin
from orders.models import *

# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
    list_display = ("name", "adress", "email", "telephone")
    list_filter = ("name",)
    
class ItemsAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "price")
    list_filter = ("name", "section",)
    
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("number", "date", "deliverer")
    list_filter = ("date",)
    date_hierarchy = "date"

admin.site.register(Clients, ClientsAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Orders, OrdersAdmin)