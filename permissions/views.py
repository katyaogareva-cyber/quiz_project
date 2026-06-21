from rest_framework.viewsets import ModelViewSet
from .models import Role, PermissionRule
from .serializers import RoleSerializer, PermissionRuleSerializer
from permissions.permissions import HasActionPermission


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    permission_classes = [HasActionPermission]

    resource = "role"


class PermissionRuleViewSet(ModelViewSet):
    queryset = PermissionRule.objects.all()
    serializer_class = PermissionRuleSerializer

    permission_classes = [HasActionPermission]

    resource = "permission_rule"
