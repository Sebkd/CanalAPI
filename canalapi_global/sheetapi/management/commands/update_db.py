from django.core.management import BaseCommand

from sheetapi.put_db import put_db

from sheetapi.models import Spreadscheet


class Command(BaseCommand):

    def handle(self, *args, **options):
        put_db(is_update=True)
        Spreadscheet.objects.filter(is_update=False).update(is_active=False)
        Spreadscheet.objects.all().update(is_update=False)
