from uuid import uuid4

from django.db import models


# Create your models here.
from canalapi.sheetapi.currency import get_currency
from canalapi.sheetapi.sheet import get_sheet


class Sheet(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    number = models.IntegerField()
    order = models.TextField(unique=True)
    cost_dollars = models.IntegerField()
    delivery_time = models.DateField()
    cost_ru = models.IntegerField(blank=True)

    def put_db(self):
        query = Sheet.delete.all()
        query.execute()
        data = get_sheet()
        currency = int(get_currency())
        for line in data[1:]:
            query = Sheet(
                {'number': int(line[0]),
                 'order': line[1],
                 'cost_dollars': line[2],
                 'delivery_time': line[3],
                 'cost_ru': int(line[2]) * currency
                 })