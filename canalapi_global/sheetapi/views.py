from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from canalapi.tasks import update_db_delay
from sheetapi.models import Spreadscheet

from sheetapi.serializers import SheetModelSerializer, SimpleSheetModelSerializer

"""просто получение данных с базы"""


class GetSheetCustomMixinViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    # update_db_delay.delay(Spreadscheet)
    queryset = Spreadscheet.objects.all()
    serializer_class = SimpleSheetModelSerializer
