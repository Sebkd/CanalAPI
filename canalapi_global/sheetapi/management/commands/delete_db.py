from django.core.management import BaseCommand

# from sheetapi.operation_db import delete_db

from sheetapi.models import Spreadscheet


class Command(BaseCommand):

    def handle(self, *args, **options):
        # delete_db()
        Spreadscheet.objects.all().delete()
