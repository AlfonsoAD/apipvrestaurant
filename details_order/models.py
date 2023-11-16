from django.db import models
from orders.models import Order
from products.models import Product


class DetailsOrder(models.Model):
    articles_count = models.IntegerField()
    unit_price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.OneToOneField(
        Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.order} {self.product} {self.articles_count}"
