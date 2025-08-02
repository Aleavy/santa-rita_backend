from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet
from django.urls import include, path

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
