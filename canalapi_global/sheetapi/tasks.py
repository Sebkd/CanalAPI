import datetime

from celery import app
from django.db.models import Q

from sheetapi.put_db import put_db


@app.shared_task
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


@app.shared_task
def update_db(cls):
    """
    Обновление базы (по идеи еще проверит на просроченную дату)
    :param cls: класс
    :return: без
    """
    put_db(cls, is_update=True)
    cls.objects.filter(is_update=False).update(is_active=False)  # помечаем удаленные как не активные
    cls.objects.all().update(is_update=False)
    print('update')
