from django.db import models
from django.contrib.auth import get_user_model
from SHOP.models import Items
from django.db.models import F, Sum, FloatField

# Create your models here.

User = get_user_model()

class Orders (models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.ordersline_set.aggregate(
            total = Sum(F("price")*F("quantity"), output_field = FloatField)
        )["total"]
    
    class Meta:
        db_table = "orders"
        verbose_name = "order"
        verbose_name_plural = "orders"
        ordering = ["id"]
    
#
class OrdersLine (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} units of {self.item.name}"
    
    class Meta:
        db_table = "ordersline"
        verbose_name = "order line"
        verbose_name_plural = "orders line"
        ordering = ["id"]
    
