from django.core.management.base import BaseCommand

from bot.telebot import runbot


class Command(BaseCommand):
    def handle(self, *args, **options):
        runbot()