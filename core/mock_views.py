USERS = [
    {"id": 1, "email": "admin@test.com", "role": "admin"},
    {"id": 2, "email": "user@test.com", "role": "viewer"},
]

PERMISSIONS = {
    "admin": {
        "user": ["read", "create", "update", "delete"],
        "role": ["read", "create", "update", "delete"],
    },
    "viewer": {
        "user": ["read"],
    }
}
