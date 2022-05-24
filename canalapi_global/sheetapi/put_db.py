from sheetapi.get_sheet import get_sheet
from sheetapi.get_currency import get_currency
from dateutil.parser import parse


def put_db(cls, is_update=False):
    """
    Загрузка данных в базу, еще и проверит на предмет просроченной даты
    :param cls: класс
    :param is_update: было обновление или нет (флаг нужный для пометки удаленных счетов)
    :return: без
    """
    data = get_sheet()
    currency = float(get_currency().replace(',', '.'))
    for line in data[1:]:
        spreadscheet_data = {
            'number': int(line[0]),
            'order': line[1],
            'cost_dollars': line[2],
            'delivery_time': parse(line[3]).date(),
            'cost_ru': round(int(line[2]) * currency, 2),
            'is_update': is_update,
        }
        query = cls(**spreadscheet_data)
        query.save()
