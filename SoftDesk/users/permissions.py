from rest_framework.permissions import BasePermission

class ContributorPermissions(BasePermission):
    """
    Contributors can read only
    User can read, add, update or delete contributor
    """

    def has_permission(self, request, view):
        pass