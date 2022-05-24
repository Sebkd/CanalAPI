import requests
from celery import app

from sheetapi.settings import TOKEN, CHANNEL_ID

import datetime

from django.db.models import Q

from sheetapi.put_db import put_db


@app.shared_task
def send_telegram_bot(text: str):
    """
    Отправка сообщения телеграм-ботом
    :param text: текст
    :return: удалось/не удалось
    """
    token = TOKEN
    url = "https://api.telegram.org/bot"
    channel_id = CHANNEL_ID
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        print("post_text error")
        return False
    else:
        print("post_text succes")
        return True


@app.shared_task
def verify_delivery_time(cls):
    """
    Проверка просроченный даты из класса
    :param cls: класс
    :return: без
    """
    pass
    # queryset = cls.objects.filter(
    #     Q(delivery_time__lte=datetime.date.today()) &
    #     Q(is_send_telegram=False))
    # for query in queryset:
    #     query.save()


@app.shared_task
def update_db_delay(cls):
    """
    Обновление базы (по идеи еще проверит на просроченную дату)
    :param cls: класс
    :return: без
    """
    put_db(cls, is_update=True)
    cls.objects.filter(is_update=False).update(is_active=False)  # помечаем удаленные как не активные
    cls.objects.all().update(is_update=False)
    print('update')
