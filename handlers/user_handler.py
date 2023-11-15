from django.core.exceptions import ValidationError


def validate_roles(value):
    allowed_roles = ["admin", "cashier", "waiter"]
    for role in value:
        if role not in allowed_roles:
            raise ValidationError(f"{role} tt is not an allowed role.")


def include_role(role: str, list_roles: list):
    return role in list_roles


def activate_role_user(user, roles: list):
    role = "admin"
    if include_role(role, roles):
        user.is_superuser = True
        user.is_staff = True
    else:
        user.is_superuser = False
        user.is_staff = False

    return user
