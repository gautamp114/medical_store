from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_anonymous:
            return False
        elif user.is_admin:
            return True
        return False

class IsAllUser(permissions.BasePermission):
    def has_permission(self,request,view):
        user = request.user
        if user.is_anonymous:
            return False
        elif user.is_admin or user.is_vendor or user.is_customer:
            return True
        return False