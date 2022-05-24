from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
# from celery.schedules import crontab

from canalapi.settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

# from canalapi.tasks import verify_delivery_time, update_db_delay
# from sheetapi.models import Spreadscheet

# from configurations import importer

import datetime
from django.db.models import Q
from sheetapi.put_db import put_db

from celery.schedules import crontab
from sheetapi.models import Spreadscheet


"""
Модуль необходимый для асинхронной работы передачи данных Телеграм-ботом и 
периодических задач по обновлению базы и проверки просроченной даты поставки
Запускаем
redis-server
из папки CanalAPI/canalapi_global$ 
celery -A canalapi.celery worker --loglevel=debug --concurrency=4
celery -A canalapi.celery beat
celery -A canalapi.celery flower --address=127.0.0.6 --port=5555
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canalapi.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')
# import canalapi.tweak_settings
# importer.install()
app = Celery('canalapi-v2', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


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
