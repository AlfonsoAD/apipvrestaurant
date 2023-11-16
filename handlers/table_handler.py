from django.core.exceptions import ValidationError


def validate_status_table(value):
    allowed_roles = ["available", "busy", "outService"]
    for role in value:
        if role not in allowed_roles:
            raise ValidationError(f"{role} it is not an allowed role.")
