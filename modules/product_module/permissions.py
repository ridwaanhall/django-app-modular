ROLE_PERMISSIONS = {
    'manager': ['create', 'read', 'update', 'delete'],
    'user': ['create', 'read', 'update'],
    'public': ['read'],
}

def has_permission(role, action):
    return action in ROLE_PERMISSIONS.get(role, [])