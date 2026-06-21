from django.db import models
from users.models import Role


class PermissionRule(models.Model):
    class Action(models.TextChoices):
        READ = "read", "Read"
        CREATE = "create", "Create"
        UPDATE = "update", "Update"
        DELETE = "delete", "Delete"

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    resource = models.CharField(max_length=100)
    action = models.CharField(max_length=10, choices=Action.choices)
