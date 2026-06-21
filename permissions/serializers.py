from rest_framework import serializers
from .models import Role, PermissionRule


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class PermissionRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionRule
        fields = "__all__"
