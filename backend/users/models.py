from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.exceptions import ValidationError


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        max_length=254
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    class Meta:
        ordering = ['email']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=('username', 'email'),
                name='unique_user'
            )
        ]

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        related_name='follower',
        verbose_name='Подписчик',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        related_name='following',
        verbose_name='Автор',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-author_id']
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'user'],
                name='unique_follower')
        ]

    def __str__(self):
        return f'Автор: {self.author}, подписчик: {self.user}'

    def save(self, **kwargs):
        if self.user == self.author:
            raise ValidationError('Невозможно подписаться на себя')
        super().save()
