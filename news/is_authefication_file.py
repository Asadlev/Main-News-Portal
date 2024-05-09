from rest_framework import generics, permissions


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
       Custom permission to only allow authenticated users to modify objects.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
