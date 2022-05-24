import requests
from canalapi.celery import app
from sheetapi.settings import TOKEN, CHANNEL_ID
import datetime
from django.db.models import Q
from sheetapi.put_db import put_db

from celery.schedules import crontab
from sheetapi.models import Spreadscheet


@app.task
def send_telegram_bot(text):
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
    print(f'send_telegram_bot - 1')
    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })
    print(f'send_telegram_bot - 2')
    if r.status_code != 200:
        print("post_text error")
        return False
    else:
        print("post_text succes")
        return True


@app.task
def verify_delivery_time(cls):
    """
    Проверка просроченный даты из класса
    :param cls: класс
    :return: без
    """

    queryset = cls.objects.filter(
        Q(delivery_time__lte=datetime.date.today()) &
        Q(is_send_telegram=False))
    for query in queryset:
        query.save()


@app.task
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


@app.on_after_configure.connect
def setup_periodic_task(sender, **kwargs):
    # периодическая проверка просроченной даты в 9 часов 30 мин
    sender.add_periodic_task(
        # crontab(30.0),
        crontab(hour=9, minute=30),
        verify_delivery_time(cls=Spreadscheet)
    )

    # периодическая проверка обновления базы 1р/2час? c 8 до 18
    sender.add_periodic_task(
        crontab(minute=0, hour='*/2, 8-18'),
        update_db_delay(cls=Spreadscheet)
    )