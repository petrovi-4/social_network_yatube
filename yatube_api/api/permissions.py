from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    def has_objects_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user)
