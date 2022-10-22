from django.db import models


class Ingredient(models.Model):
    """Класс ингредиентов"""
    name = models.CharField(
        verbose_name='Название ингридиента',
        max_length=30
    )
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=30
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


class IngredientRecipe(models.Model):
    """Вспомогательный класс, который связывает ингредиенты и рецепты"""

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient_amounts',
        verbose_name='Ингредиент'
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name='ingredient_amounts',
        verbose_name='Рецепт'
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество'
    )

    class Meta:
        pass

    def __str__(self):
        return f'{self.ingredient}, {self.recipe}'


class Recipe(models.Model):
    """Класс рецептов"""

    name = models.CharField(
        max_length=200,
        verbose_name='Название рецепта'
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        related_name='recipes',
        verbose_name='Ингредиент'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'
