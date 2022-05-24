from django.core.management import BaseCommand


from sheetapi.operation_db import update_db


class Command(BaseCommand):

    def handle(self, *args, **options):
        update_db()
