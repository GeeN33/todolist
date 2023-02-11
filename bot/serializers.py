from rest_framework import serializers
from bot.models import TgUser

class  TgUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TgUser
        fields = ['verification_code']

    def is_valid(self, *, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)





