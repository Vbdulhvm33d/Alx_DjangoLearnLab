from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.authentication import TokenAuthentication

class isAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to edit objects.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
    
class IsAuthenticated(IsAuthenticated):
    authentication_classes = [TokenAuthentication]