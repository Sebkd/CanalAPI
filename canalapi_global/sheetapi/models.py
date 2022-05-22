from django.db import models

# Create your models here.
from django.utils import timezone


class Spreadscheet(models.Model):
    class Meta:
        app_label = 'sheetapi'

    number = models.IntegerField()
    order = models.TextField(primary_key=True, unique=True)
    cost_dollars = models.IntegerField()
    delivery_time = models.DateField()
    cost_ru = models.FloatField(blank=True)
    is_change = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, auto_created=True)
    is_created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
