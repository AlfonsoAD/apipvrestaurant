from django.db import models
from users.models import User
from box_oppenings.models import BoxOppening


class BoxCut(models.Model):
    total_ammount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_made_cut = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,)
    box_openning = models.OneToOneField(
        BoxOppening, on_delete=models.SET_NULL, null=True,)

    def __str__(self) -> str:
        return f"{self.user_made_cut} - {self.total_ammount}"
