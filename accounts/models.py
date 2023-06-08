from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    natioality = models.CharField(max_length=255)
    User_name = models.CharField(max_length=255)
    cell_phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    company = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',  # 加入 related_name 參數
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',  # 加入 related_name 參數
        related_query_name='user'
    )
