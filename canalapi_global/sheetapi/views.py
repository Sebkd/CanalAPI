from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from sheetapi.models import Spreadscheet
from sheetapi.serializers import SheetModelSerializer

from sheetapi.models import put_db


class GetSheetCustomMixinViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    # put_db()
    queryset = Spreadscheet.objects.all()
    serializer_class = SheetModelSerializer
