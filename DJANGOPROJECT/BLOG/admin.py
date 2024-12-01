from django.contrib import admin
from .models import Categories, Posts

# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    

class PostssAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
    
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Posts, PostssAdmin)