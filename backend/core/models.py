from django.core import validators
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    '''Класс пользователей.'''

    username = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        unique=True,
        db_index=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Имя пользователя содержит недопустимый символ'
        )]
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='Email',
        unique=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return f'{self.username}'


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
        ordering = ('id',)

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
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ('id',)

    def __str__(self):
        return f'{self.ingredient}, {self.recipe}'


class Tag(models.Model):
    """Класс для тэгов"""

    name = models.CharField(
        max_length=256,
        verbose_name='Наименование тэга'
    )
    color = models.CharField(
        max_length=10,
        verbose_name='Цвет тэга'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Слаг тэга'
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    """Класс рецептов"""

    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тэги',
    )
    author = models.ForeignKey(
        User,
        related_name='recipes',
        verbose_name='Автор',
        null=True,
        on_delete=models.SET_NULL
    )
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
    # image = models.ImageField(
    #     verbose_name='Фото'
    # )
    # text = models.TextField(
    #     verbose_name='Описание'
    # )
    # cooking_time = models.PositiveIntegerField(
    #     verbose_name='время приготовления',
    #     validators=[validators.MinValueValidator(
    #         1, message='Минимальное время приготовления 1 минута'),
    #     ]
    # )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'author'],
                name='unique_recipe'),
        ]

    def __str__(self):
        return f'{self.name}'


class Follow(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_follow',
            )
        ]

    def __str__(self):
        return f'{self.author }'


class Favorite(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Автор'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Рецепт в избранном'
    )

    class Meta:
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'recipe'],
                name='unique_favorite'),
        ]

    def __str__(self):
        return f'{self.author }'


class ShoppingCart(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Автор'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'recipe'],
                name='unique_cart_recipe'),
        ]

    def __str__(self):
        return f'{self.author }'
