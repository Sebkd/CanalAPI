from sheetapi.models import Spreadscheet
from sheetapi.put_db import put_db


def create_db():
    """
    Создание базы, низкий уровень, для использования в составе команд python manage.py
    :return: без
    """
    Spreadscheet.objects.all().delete()
    put_db(cls=Spreadscheet)


def delete_db():
    """
    Удаление базы, низкий уровень, для использования в составе команд python manage.py
    :return: без
    """
    Spreadscheet.objects.all().delete()
    return True


def update_db():
    """
        Обновление базы, низкий уровень, для использования в составе команд python manage.py
        :return: без
        """
    put_db(cls=Spreadscheet, is_update=True)
    Spreadscheet.objects.filter(is_update=False).update(is_active=False)  # помечаем удаленные как не активные
    Spreadscheet.objects.all().update(is_update=False)
    print('update')
