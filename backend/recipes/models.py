from django.db import models

from users.models import User


class Ingridient(models.Model):
    title = models.CharField(max_length=100)
    amount = models.SmallIntegerField(blank=True)
    measurement_unit = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title} - {self.amount} {self.measurement_unit}'


class Tag(models.Model):
    title = models.CharField(verbose_name='Тэг', max_length=100, unique=True)
    hexcolor = models.CharField(max_length=7, default="#ffffff", unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )
    title = models.CharField(
        verbose_name='Название блюда',
        max_length=200,
    )
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='recipes/'
    )
    text = models.TextField(
        verbose_name='Описание рецепта'
    )
    ingridients = models.ManyToManyField(
        Ingridient,
        related_name='recipes',
        verbose_name='Ингридиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тэги'
    )
    time = models.TimeField(
        verbose_name='Временные затраты'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeIngridient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )
    ingridient = models.ForeignKey(
        Ingridient,
        on_delete=models.CASCADE
    )
    quantity = models.DecimalField(
        verbose_name='Количество',
        max_digits=4,
        decimal_places=1
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('recipe', 'ingridient'),
                name='uniqe_ingridient_in_recipe'
            )
        ]

class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=(
                    'user',
                    'recipe'
                ),
                name='unique_favorite'
            )
        ]