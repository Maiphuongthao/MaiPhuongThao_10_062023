from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CommentPermisson(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author_user_id == request.user
