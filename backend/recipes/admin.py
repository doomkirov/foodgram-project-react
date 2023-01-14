from django.contrib import admin

from .models import (
    Ingridient, Recipe, Tag,
    RecipeIngridient, Favorite, ShoppingCart
)


class IngridientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'pub_date', 'display_tags', 'favorite')
    list_filter = ('name', 'author', 'tags')
    search_fields = ('name',)
    readonly_fields = ('favorite',)
    fields = (
        'image',
        ('name', 'author'),
        'text',
        ('tags', 'cooking_time'),
        'favorite'
    )

    def display_tags(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Теги'

    def favorite(self, obj):
        return obj.favorite.count()
    favorite.short_description = 'Тег в избранном'


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')


admin.site.register(Ingridient, IngridientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(RecipeIngridient, RecipeIngredientAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
