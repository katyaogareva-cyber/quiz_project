from django.contrib import admin
from .models import Role, PermissionRule

admin.site.register(PermissionRule)
admin.site.register(Role)
