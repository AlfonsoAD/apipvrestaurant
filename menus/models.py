from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name - self.description}"
