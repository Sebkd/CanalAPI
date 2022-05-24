from django.core.management import BaseCommand

from sheetapi.operation_db import create_db


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_db()
