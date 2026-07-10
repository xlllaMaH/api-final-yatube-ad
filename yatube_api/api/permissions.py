"""Permissions for api."""
from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Only author can change object."""

    def has_permission(self, request, view):
        """Check authenticated or request method."""
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        """Check user is author."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class ReadOnly(permissions.BasePermission):
    """Only read for non-authenticated."""

    def has_permission(self, request, view):
        """Check request method."""
        return request.method in permissions.SAFE_METHODS
