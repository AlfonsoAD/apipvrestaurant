from django.db import models
from orders.models import Order


class Sale(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_sale = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id} - {self.total_sale} - {self.order}"
