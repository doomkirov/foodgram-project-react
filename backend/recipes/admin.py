from django.contrib import admin
from django.contrib.admin.filters import AllValuesFieldListFilter

from .models import Ingridient, Recipe, Tag
from .forms import RecipeForm


class IngridientAdmin(admin.ModelAdmin):
    list_display = (
    'pk',
    'title',
    'amount',
    'measurement_unit'
)


class RecipeAdmin(admin.ModelAdmin):
    form = RecipeForm
    list_filter = ('tags',)
    list_display = (
        'author',
        'title',
        'image',
        'text',
        'time',
    )
    list_editable = (
        'title',
        'time'
    )
    search_fields = (
        'title',
    )


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'hexcolor',
        'slug'
    )


admin.site.register(Ingridient, IngridientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)