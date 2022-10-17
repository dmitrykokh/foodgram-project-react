from django.db import models


class Ingredient(models.Model):
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


# class IngredientRecipe(models.Model):
#
#
# class Recipe(models.Model):

