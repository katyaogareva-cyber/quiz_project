from users.models import Role
from permissions.models import BusinessElement, AccessRolesRules


def run():
    admin = Role.objects.get(name="admin")
    editor = Role.objects.get(name="editor")
    viewer = Role.objects.get(name="viewer")

    user_el, _ = BusinessElement.objects.get_or_create(name="user")
    role_el, _ = BusinessElement.objects.get_or_create(name="role")

    AccessRolesRules.objects.get_or_create(
        role=admin,
        element=user_el,
        defaults=dict(
            read_permission=True,
            create_permission=True,
            update_permission=True,
            delete_permission=True,
            read_all_permission=True,
        )
    )

    AccessRolesRules.objects.get_or_create(
        role=viewer,
        element=user_el,
        defaults=dict(
            read_permission=True,
        )
    )
