import os

import canalapi.tweak_settings
from celery import Celery
from celery.schedules import crontab

from canalapi.settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
from canalapi.tasks import verify_delivery_time, update_db_delay
from sheetapi.models import Spreadscheet

"""
Модуль необходимый для асинхронной работы передачи данных Телеграм-ботом и 
периодических задач по обновлению базы и проверки просроченной даты поставки
Запускаем
redis-server
из папки CanalAPI/canalapi_global$ 
celery -A canalapi.celery worker --loglevel=debug --concurrency=4
celery -A canalapi.celery beat
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canalapi.settings')

app = Celery('canalapi-v2', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_task(sender, **kwargs):
    # периодическая проверка просроченной даты в 9 часов 30 мин
    sender.add_periodic_task(
        crontab(hour=9, minute=30),
        verify_delivery_time(cls=Spreadscheet)
    )

    # периодическая проверка обновления базы 1р/2час? c 8 до 18
    sender.add_periodic_task(
        crontab(minute=0, hour='*/2, 8-18'),
        update_db_delay(cls=Spreadscheet)
    )
