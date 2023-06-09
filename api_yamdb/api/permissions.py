from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin or request.user.is_superuser)


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and obj.author == request.user)
                or request.user.is_moderator or request.user.is_admin
                )
