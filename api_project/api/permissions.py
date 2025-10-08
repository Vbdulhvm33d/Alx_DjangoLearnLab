from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class isAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
    
class IsAuthenticated(IsAuthenticated):
    authentication_classes = [TokenAuthentication]
