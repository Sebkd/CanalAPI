import datetime

from dateutil.parser import parse
from django.db import models


# Create your models here.
from sheetapi.currency import get_currency
from sheetapi.sheet import get_sheet


class Spreadscheet(models.Model):
    class Meta:
        app_label = 'sheet_table'

    number = models.IntegerField()
    order = models.TextField(primary_key=True, unique=True)
    cost_dollars = models.IntegerField()
    delivery_time = models.DateField()
    cost_ru = models.FloatField(blank=True)


def put_db():
    # query_set = Sheet.objects.all()
    # print()
    # print(len(query_set))
    # print()
    # for query in query_set:
    #     query.delete()
    #     query.execute()
    data = get_sheet()
    currency = float(get_currency().replace(',', '.'))
    for line in data[1:]:
        date = parse(line[3]).date()
        query = Spreadscheet(int(line[0]),
                             line[1],
                             line[2],
                             parse(line[3]).date(),
                             int(line[2]) * currency
                             )
        query.save()