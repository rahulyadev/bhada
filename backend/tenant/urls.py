from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TenantViewSet

router = DefaultRouter()
router.register("", TenantViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
