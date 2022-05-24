import datetime
import canalapi.settings
from django.db import models
from django.db.models import signals

# Create your models here.
from django.utils import timezone
from canalapi.tasks import send_telegram_bot


class Spreadscheet(models.Model):
    class Meta:
        app_label = 'sheetapi'

    number = models.IntegerField()
    order = models.TextField(primary_key=True, unique=True)
    cost_dollars = models.IntegerField()
    delivery_time = models.DateField()
    cost_ru = models.FloatField(blank=True)
    is_change = models.DateTimeField(auto_now=True)
    is_update = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, auto_created=True)

    is_overdate = models.BooleanField(default=False)
    is_send_telegram = models.BooleanField(default=False)


def spreadscheet_pre_save(sender, instance, signal, *args, **kwargs):
    """Проверка просроченной даты перед изменением базы"""
    if instance.delivery_time > datetime.date.today() and \
            instance.is_send_telegram == False and \
            instance.is_active == True:
        instance.is_overdate = True
        # if send_telegram_bot.delay(f'Просроченный заказ {instance.order}, '
        #                         f'дата поставки {str(instance.delivery_time)}, '
        #                         f'сумма, руб: {instance.cost_ru}'):
        instance.is_send_telegram = True


    # queryset = Spreadscheet.objects.filter(
    #     Q(delivery_time__lte=datetime.date.today()) &
    #     # Q(is_overdate=False) &
    #     Q(is_send_telegram=False))
    # for query in queryset:
    #     query.is_overdate = True
    #     if send_telegram_bot.delay(f'Просроченный заказ {query.order}, '
    #                                f'дата поставки {str(query.delivery_time)}, '
    #                                f'сумма, руб: {query.cost_ru}'):
    #         query.is_send_telegram = True
    #     query.save()


signals.pre_save.connect(spreadscheet_pre_save, sender=Spreadscheet)
