from rest_framework.serializers import ModelSerializer

from canalapi.sheetapi.models import Sheet
from canalapi.sheetapi.sheet import get_sheet


class SheetModelSerializer(ModelSerializer):
    class Meta:
        model = Sheet
        fields = '__all__'

