from django.core.management import BaseCommand

from sheetapi.models import Spreadscheet


class Command(BaseCommand):

    def handle(self, *args, **options):
        Spreadscheet.objects.all().delete()
