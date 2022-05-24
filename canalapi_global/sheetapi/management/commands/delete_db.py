from django.core.management import BaseCommand

from sheetapi.operation_db import delete_db


class Command(BaseCommand):

    def handle(self, *args, **options):
        delete_db()
