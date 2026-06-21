from rest_framework.permissions import BasePermission
from .models import PermissionRule

class HasActionPermission(BasePermission):

    ACTION_MAP = {
        "list": "read",
        "retrieve": "read",
        "create": "create",
        "update": "update",
        "partial_update": "update",
        "destroy": "delete",
    }

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        action = self.ACTION_MAP.get(getattr(view, "action", None))
        resource = getattr(view, "resource", None)

        if not action or not resource:
            return False

        return PermissionRule.objects.filter(
            role__in=user.roles.all(),
            resource=resource,
            action=action
        ).exists()
