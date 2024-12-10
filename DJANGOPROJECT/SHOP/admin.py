from django.contrib import admin
from .models import ShopCategories, Items

# Register your models here.


class ShopCategoriesAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    

class ItemsAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
    
admin.site.register(ShopCategories, ShopCategoriesAdmin)
admin.site.register(Items, ItemsAdmin)