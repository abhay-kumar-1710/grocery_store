from rest_framework.permissions import BasePermission

# FOR MANAGER
class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated  and request.user.role == "manager"

# FOR CUSTOMER
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated  and request.user.role == "customer"