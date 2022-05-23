import datetime

from django.core.management import BaseCommand
from django.db.models import Q
from django.utils import timezone

from sheetapi.models import Spreadscheet


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Получаем queryset, где у нас превышена дата + нет флага о превышении +
        не отправляли в телеграм"""
        queryset = Spreadscheet.objects.filter(
            Q(delivery_time__gte=datetime.date.today()) &
            Q(is_overdate=False) &
            Q(is_send_telegram=False))


