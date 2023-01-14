from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    IngridientViewSet,
    RecipeViewSet,
    TagViewSet,
)


app_name = 'api'

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ingredients', IngridientViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
