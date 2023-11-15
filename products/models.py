from django.db import models
from cloudinary.models import CloudinaryField
from categorys.models import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = CloudinaryField('image')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    category = models.OneToOneField(
        Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
