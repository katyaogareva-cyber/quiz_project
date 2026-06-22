from rest_framework.viewsets import ModelViewSet
from .models import Role, AccessRolesRules
from .serializers import RoleSerializer, AccessRolesRulesSerializer
from permissions.permissions import HasAccessPermission


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [HasAccessPermission]
    element = "role"


class AccessRolesRulesViewSet(ModelViewSet):
    queryset = AccessRolesRules.objects.all()
    serializer_class = AccessRolesRulesSerializer
    permission_classes = [HasAccessPermission]
    element = "access_rules"
