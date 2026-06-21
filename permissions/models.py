from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class PermissionRule(models.Model):
    class Action(models.TextChoices):
        READ = "read", "Read"
        CREATE = "create", "Create"
        UPDATE = "update", "Update"
        DELETE = "delete", "Delete"

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    resource = models.CharField(max_length=100)
    action = models.CharField(max_length=10, choices=Action.choices)

    def __str__(self):
        return f"{self.role} → {self.resource} → {self.action}"
