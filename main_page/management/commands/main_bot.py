from django.core.management.base import BaseCommand
from django.conf import settings
### Telebot import ###
import telebot


class Command(BaseCommand):
    help = 'Бот'

    def handle(self, *args, **options):
        from main_page.bot import bot
        #from bot import keyboards
        print(bot.get_me())

        bot.polling(none_stop=True)

