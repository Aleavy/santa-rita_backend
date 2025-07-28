from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from django.urls import include, path

router = DefaultRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
