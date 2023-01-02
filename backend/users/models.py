from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLE = 'user'
    ADMIN_ROLE = 'admin'
    ROLES = [
        (USER_ROLE, 'User'),
        (ADMIN_ROLE, 'Administrator'),
    ]
    confirmation_code = models.CharField(
        'Код подтверждения', blank=True, max_length=50
    )
    role = models.CharField(
        'Роль', max_length=50, choices=ROLES, default='user'
    )

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    @property
    def is_admin(self):
        return self.role == 'admin'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name='unique_user_email'),
        ]
        ordering = ['id']


class Follow(models.Model):
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['follower', 'following'],
                name='unique_follow'
            ),
        ]
