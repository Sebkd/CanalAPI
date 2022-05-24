from rest_framework.serializers import ModelSerializer

from sheetapi.models import Spreadscheet


class SheetModelSerializer(ModelSerializer):
    """
    Сериализатор для вывода всех полей
    """

    class Meta:
        model = Spreadscheet
        fields = '__all__'


class SimpleSheetModelSerializer(ModelSerializer):
    """
    Сериализатор для вывода  полей по заданию
    """

    class Meta:
        model = Spreadscheet
        fields = ('number', 'order', 'cost_dollars', 'delivery_time', 'cost_ru')
