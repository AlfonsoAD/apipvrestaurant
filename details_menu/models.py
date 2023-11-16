from django.db import models
from menus.models import Menu
from products.models import Product


class DetailsMenu(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.OneToOneField(
        Product, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.menu} - {self.product}"
