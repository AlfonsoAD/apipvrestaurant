from rest_framework import permissions

role_admin = "admin"
role_cashier = "cashier"
role_waiter = "waiter"


class IsAdminRoleUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and role_admin in request.user.roles


class IsCashierRoleUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (role_cashier in request.user.roles or role_admin in request.user.roles)


class IsWaiterRoleUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (role_waiter in request.user.roles or role_admin in request.user.roles)
