from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from sheetapi.models import Spreadscheet
from sheetapi.operation_db import update_db, overdate_transfer
from sheetapi.serializers import SheetModelSerializer


class GetSheetCustomMixinViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    update_db()
    overdate_transfer()
    queryset = Spreadscheet.objects.all()
    serializer_class = SheetModelSerializer
