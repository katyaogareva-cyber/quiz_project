def has_permission(role, element, action):
    role_permissions = PERMISSIONS.get(role, {})
    allowed_actions = role_permissions.get(element, [])
    return action in allowed_actions
