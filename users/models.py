from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)

    email = models.EmailField(verbose_name='email', unique=True)
    first_name = models.CharField(max_length=45, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=45, verbose_name='имя', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)
    is_staff = models.BooleanField(default=False, verbose_name='сотрудник')
    is_active = models.BooleanField(default=True, verbose_name='активность')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'Пользователь - {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
