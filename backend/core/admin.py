from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (Favorite, Follow, Ingredient, IngredientRecipe,
                     Recipe, ShoppingCart, Tag, User)


class CustomUserAdmin(UserAdmin):
    search_fields = ('username', 'email', 'first_name')
    list_filter = ('username', 'email', 'first_name')


class RecipeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'author', 'tags', 'text')
    list_filter = ('name', 'author', 'tags')
    list_display = (
        'name',
        'author',
        'text',
        'image',
        'cooking_time',
        'count_favorites'
    )

    def count_favorites(self, obj):
        return obj.favorites.count()

    count_favorites.description = 'Число добавлений в избранное'


class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('ingredient_name', )
    list_filter = ('ingredient_name', )


admin.site.empty_value_display = 'значение не задано'
admin.site.register(Tag)
admin.site.register(IngredientRecipe)
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
admin.site.register(Follow)
admin.site.register(User, CustomUserAdmin)
