from rest_framework import permissions


class IsAdminOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 'admin'
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.role == 'admin'
        return False
