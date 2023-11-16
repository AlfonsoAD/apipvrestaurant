from django.db import models
from details_order.models import DetailsOrder


class ProductNotes(models.Model):
    note = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    details_order = models.OneToOneField(
        DetailsOrder, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.note} {self.details_order}"
