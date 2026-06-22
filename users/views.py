from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from permissions.permissions import HasAccessPermission


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [HasAccessPermission]

    element = "user"

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(status=204)
