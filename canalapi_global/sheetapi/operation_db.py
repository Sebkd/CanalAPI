import datetime

from django.db.models import Q
from sheetapi.models import Spreadscheet
from sheetapi.put_db import put_db
from sheetapi.send_telegram import send_telegram


def create_db():
    Spreadscheet.objects.all().delete()
    put_db()


def delete_db():
    Spreadscheet.objects.all().delete()
    return True


def update_db():
    put_db(is_update=True)
    Spreadscheet.objects.filter(is_update=False).update(is_active=False)
    Spreadscheet.objects.all().update(is_update=False)


def overdate_transfer():
    """ Получаем queryset, где у нас превышена дата + нет флага о превышении +
    не отправляли в телеграм"""
    queryset = Spreadscheet.objects.filter(
        Q(delivery_time__gte=datetime.date.today()) &
        Q(is_overdate=False) &
        Q(is_send_telegram=False))
    for query in queryset:
        query.is_overdate = True
        send_telegram(f'Просроченный заказ {query.order}, дата поставки {str(query.delivery_time)}, сумма, руб: {query.cost_ru}')
        query.is_send_telegram = True
        query.save()
        print()
