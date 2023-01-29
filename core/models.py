from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    # username = models.CharField(null=True, max_length=50)
    # email = models.CharField(null=True, max_length=50)
    # first_name = models.CharField(null=True, max_length=50)
    # last_name = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["username"]
