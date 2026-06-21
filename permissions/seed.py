from users.models import Role
from permissions.models import PermissionRule

def run():
    admin = Role.objects.get(name="admin")
    editor = Role.objects.get(name="editor")
    viewer = Role.objects.get(name="viewer")

    rules = [
        (admin, "role", "create"),
        (admin, "role", "read"),
        (admin, "role", "update"),
        (admin, "role", "delete"),

        (admin, "user", "read"),
        (editor, "user", "update"),
        (viewer, "user", "read"),

        (admin, "permissionrule", "create"),
        (admin, "permissionrule", "read"),
        (admin, "permissionrule", "update"),
        (admin, "permissionrule", "delete"),
    ]

    for role, resource, action in rules:
        PermissionRule.objects.get_or_create(
            role=role,
            resource=resource,
            action=action
        )
