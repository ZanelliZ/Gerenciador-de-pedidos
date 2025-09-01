from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
# products/urls.py
router = DefaultRouter()
router.register(r'', ProductViewSet, basename='produto') # ✅ CORRIGIDO

urlpatterns = [
    path('', include(router.urls)),
]