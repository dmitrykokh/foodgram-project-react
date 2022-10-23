from django.shortcuts import render
from rest_framework import viewsets

from backend.api.serializers import IngredientSerializer
from backend.core.models import Ingredient, Recipe


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет ингредиентов"""

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с объектами класса Recipe"""

    queryset = Recipe.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    pagination_classes = CustomPagination


    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return RecipeSerializer
        return RecipeCreateSerializer

    @staticmethod
    def create_object(request, pk, serializer):