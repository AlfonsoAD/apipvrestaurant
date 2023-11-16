from django.core.exceptions import ValidationError


def validate_status(value):
    allowed_roles = ["orderActive", "orderPending", "orderCompleted"]
    for role in value:
        if role not in allowed_roles:
            raise ValidationError(f"{role} it is not an allowed role.")
