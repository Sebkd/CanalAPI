from django.core.management import BaseCommand

from sheetapi.put_db import put_db


class Command(BaseCommand):

    def handle(self, *args, **options):
        put_db()
