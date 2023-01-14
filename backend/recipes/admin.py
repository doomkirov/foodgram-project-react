from django.contrib import admin
from django.contrib.admin.filters import AllValuesFieldListFilter

from .models import Ingridient, Recipe, Tag
from .forms import RecipeForm


class IngridientAdmin(admin.ModelAdmin):
    list_display = (
    'pk',
    'name',
    'measurement_unit'
)


class RecipeAdmin(admin.ModelAdmin):
    form = RecipeForm
    list_filter = ('tags',)
    list_display = (
        'author',
        'name',
        'image',
        'text',
        'time',
    )
    list_editable = (
        'name',
        'time'
    )
    search_fields = (
        'name',
    )


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'hexcolor',
        'slug'
    )


admin.site.register(Ingridient, IngridientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)