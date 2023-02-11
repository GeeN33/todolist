import json
import os
import time
from django.db.models import *
import requests

from bot.models import TgMessage, TgUser
from core.models import User
from goals.models import Goal
from todolist.settings import TOKEN


URL = f'https://api.telegram.org/bot{TOKEN}/'

HELP_COMMAND = """
список команд \n
/help - список команд \n
/goals - открытые цели \n
"""

class Message():
    def __init__(self, data):
        self.date = data['message']['date']
        self.update_id = int(data['update_id'])
        self.chat_id = int(data['message']['chat']['id'])
        self.username = data['message']['chat']['username']
        self.text = data['message']['text']

    def __str__(self):
        return  self.text

def requests_tg(curl, metod):
  r =  requests.get(curl + metod).json()
  return r

def send_message(chat_id, text):
    url = URL+'sendMessage'
    answer = {'chat_id' : chat_id, 'text': text}
    r = requests.post(url,json=answer)

def parsing(data):
    max = TgMessage.objects.aggregate(Max('update_id'))['update_id__max']
    if not max: max = 0

    message_list_temp = []

    for i in data['result']:
        message_list_temp.append(Message(i))

    for m in message_list_temp:
        if m.update_id > max:
            TgMessage.objects.create(
            date=m.date,
            update_id = m.update_id,
            chat_id = m.chat_id,
            username = m.username,
            text = m.text,
            )

            reg_user = True
            for tg in TgUser.objects.all():
                if tg.tg_id == m.chat_id:
                    reg_user = False
                    if m.text == '/start':
                        send_message(tg.tg_id, "ты уже на борту")
                        send_message(m.chat_id, f"verification_code: {tg.verification_code}")
                    elif m.text == '/goals':
                        users = User.objects.get(id=tg.user_id)
                        goals = Goal.objects.filter(
                            user=users,
                            status=Goal.Status.in_progress,
                        )
                        if len(goals):
                            strrez = 'Твои цели:\n'
                            for g in goals:
                                strrez = strrez + g.title + '\n'
                            send_message(tg.tg_id, strrez)
                        else:
                            send_message(tg.tg_id, "Извини, но у тебя нет пока открытых целей")
                    elif m.text == '/help':
                        send_message(tg.tg_id, HELP_COMMAND)
                    else:
                         strrez = 'неизвестная команда\n'
                         strrez = strrez + HELP_COMMAND
                         send_message(tg.tg_id, strrez)

            if reg_user:
                if m.text == '/start':
                    code = os.urandom(8).hex()
                    TgUser.objects.create(
                        tg_id=m.chat_id,
                        verification_code=code,
                        username=m.username,
                    )

                    send_message(m.chat_id, f"verification_code: {code}")

def runbot():
    while True:
        r = requests_tg(URL, 'getUpdates?timeout=30')
        try:
            if r['ok']:
               parsing(r)
               time.sleep(5)
            else:
               time.sleep(30)

        except Exception:
             time.sleep(60)


