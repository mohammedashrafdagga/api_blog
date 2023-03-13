from rest_framework.permissions import BasePermission
from .token import get_user_token


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == get_user_token(request)
