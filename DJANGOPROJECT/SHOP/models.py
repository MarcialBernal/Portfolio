from django.db import models

# Create your models here.

class ShopCategories(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name

class Items(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(ShopCategories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="shop", null=True, blank=True)
    price = models.FloatField()
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        
    def __str__(self):
        return self.name