from rest_framework.serializers import ModelSerializer

from sheetapi.models import Spreadscheet


class SheetModelSerializer(ModelSerializer):
    class Meta:
        model = Spreadscheet
        fields = '__all__'

