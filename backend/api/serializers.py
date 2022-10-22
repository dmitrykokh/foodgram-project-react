from backend.core.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Ingredient."""

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class IngredientRecipeSerializer(serializers.ModelSerializer):
    pass


class RecipeSerializer(serializers.ModelSerializer):
    pass


class RecipeCreateSerializer(serializers.ModelSerializer):
    pass
