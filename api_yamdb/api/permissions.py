from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.role == 'admin'

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or request.user.role == 'admin'


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.role == 'user'
                    and obj.author == request.user)
                or (request.user.role in ['moderator', 'admin'])
                )
