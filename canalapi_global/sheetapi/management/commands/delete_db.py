from django.core.management import BaseCommand

from sheetapi.put_db import put_db

from sheetapi.models import Spreadscheet


class Command(BaseCommand):

    def handle(self, *args, **options):
        Spreadscheet.objects.all().delete()
