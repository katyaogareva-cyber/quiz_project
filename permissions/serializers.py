from rest_framework import serializers
from .models import Role, AccessRolesRules


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class AccessRolesRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRolesRules
        fields = "__all__"
