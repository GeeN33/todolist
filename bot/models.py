from django.db import models

from core.models import User


class TgUser(models.Model):

    tg_id = models.BigIntegerField(null=True, blank=True, default=None)
    username = models.CharField(null=True, max_length=50, blank=True, default=None)
    verification_code = models.CharField(null=True, max_length=50, blank=True, default=None)
    user_id =  models.CharField(null=True, max_length=50, blank=True, default=None)
    verification_True = models.BooleanField(null=True, blank=True, default=False)


class TgMessage(models.Model):

    date = models.CharField(null=True, max_length=50)
    update_id = models.BigIntegerField(null=True)
    chat_id = models.BigIntegerField(null=True)
    username = models.CharField(null=True, max_length=50)
    text = models.CharField(null=True, max_length=50)

