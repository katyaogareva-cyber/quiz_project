from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from permissions.views import RoleViewSet, PermissionRuleViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"roles", RoleViewSet)
router.register(r"permissions", PermissionRuleViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),

    path("api/", include(router.urls)),
]
