import datetime

from django.core.management import BaseCommand

from sheetapi.operation_db import overdate_transfer


class Command(BaseCommand):

    def handle(self, *args, **options):
        overdate_transfer()
