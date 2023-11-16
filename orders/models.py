from django.db import models
from django.contrib.postgres.fields import ArrayField
from handlers.order_handler import validate_status
from users.models import User
from tables.models import Table


class Order(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    process_status = ArrayField(models.CharField(
        max_length=50), default="orderPending", validators=[validate_status])
    priority = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    table = models.OneToOneField(Table, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.order_number} - {self.date}"
