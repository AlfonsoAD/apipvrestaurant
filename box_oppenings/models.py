from django.db import models
from users.models import User


class BoxOppening(models.Model):
    starting_ammount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_authorized = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,)

    def __str__(self) -> str:
        return f"{self.user_authorized} - {self.starting_ammount}"
