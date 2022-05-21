from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from canalapi.sheetapi.models import Sheet
from canalapi.sheetapi.serializers import SheetModelSerializer


class GetSheetCustomMixinViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    Sheet.put_db()
    queryset = Sheet.objects.all()
    serializer_class = SheetModelSerializer
