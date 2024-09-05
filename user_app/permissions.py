from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            return False
        

class CheckUserName(BasePermission):
    def has_permission(self, request, view):
        if request.user.username == 'admin':
            return True
        else:
            return False

