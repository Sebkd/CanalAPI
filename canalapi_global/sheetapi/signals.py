import datetime

# from sheetapi.models import Spreadscheet
# from django.db.models import signals
from canalapi.tasks import send_telegram_bot


def spreadscheet_pre_save(sender, instance, signal, *args, **kwargs):
    """Проверка просроченной даты перед изменением базы"""
    if instance.delivery_time < datetime.date.today() and \
            instance.is_send_telegram == False and \
            instance.is_active == True:
        instance.is_overdate = True
        msg = str(f'Просроченный заказ {instance.order}, '
                  f'дата поставки {str(instance.delivery_time)}, '
                  f'сумма, руб: {instance.cost_ru}')
        print(f'spreadscheet_pre_save - 1,\n {msg}')
        if send_telegram_bot.delay(msg):
            instance.is_send_telegram = True
            print(f'spreadscheet_pre_save - 1')
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


# signals.pre_save.connect(spreadscheet_pre_save, sender=Spreadscheet)
