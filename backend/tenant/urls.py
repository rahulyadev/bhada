from django.urls import path, include
from .views import TenantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TenantViewSet)
urlpatterns = [
    path('', include(router.urls)),
]