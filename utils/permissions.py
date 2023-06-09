from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.id == request.user or request.user.is_superuser:
            return True
        return False