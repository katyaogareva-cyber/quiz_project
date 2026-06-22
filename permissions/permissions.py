from rest_framework.permissions import BasePermission
from permissions.models import AccessRolesRules


class HasAccessPermission(BasePermission):

    def has_permission(self, request, view):

        if not request.user or not request.user.is_authenticated:
            return False

        element = getattr(view, "element", None)
        if not element:
            return False

        action_map = {
            "GET": "read_permission",
            "POST": "create_permission",
            "PUT": "update_permission",
            "PATCH": "update_permission",
            "DELETE": "delete_permission",
        }

        action = action_map.get(request.method)
        if not action:
            return False

        rules = AccessRolesRules.objects.filter(
            role__in=request.user.roles.all(),
            element__name=element
        )

        if not rules.exists():
            return False

        for rule in rules:
            if getattr(rule, action, False):
                return True

        return False
