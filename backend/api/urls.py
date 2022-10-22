from django.urls import include, path
from rest_framework import routers

from backend.api.views import IngredientViewSet, RecipeViewSet

router = routers.DefaultRouter()
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
