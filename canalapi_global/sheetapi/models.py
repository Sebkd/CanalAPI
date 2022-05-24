import canalapi.settings
from django.db import models
from django.db.models import signals


# Create your models here.
from sheetapi.signals import spreadscheet_pre_save


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


signals.pre_save.connect(spreadscheet_pre_save, sender=Spreadscheet)
