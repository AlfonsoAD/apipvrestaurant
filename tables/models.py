from django.db import models
from django.contrib.postgres.fields import ArrayField
from handlers.table_handler import validate_status_table


class Table(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    table_status = ArrayField(
        models.CharField(max_length=30),
        default="available",
        null=False,
        validators=[validate_status_table]
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.number}"
