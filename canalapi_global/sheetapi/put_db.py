from sheetapi.get_sheet import get_sheet
from sheetapi.get_currency import get_currency
from dateutil.parser import parse


from sheetapi.models import Spreadscheet


def put_db():
    data = get_sheet()
    currency = float(get_currency().replace(',', '.'))
    for line in data[1:]:
        spreadscheet_data = {
            'number': int(line[0]),
            'order': line[1],
            'cost_dollars': line[2],
            'delivery_time': parse(line[3]).date(),
            'cost_ru': int(line[2]) * currency,
        }
        print(spreadscheet_data)
        # query = Spreadscheet(int(line[0]),
        #                      line[1],
        #                      line[2],
        #                      parse(line[3]).date(),
        #                      int(line[2]) * currency
        #                      )
        # query.save()
        query = Spreadscheet(**spreadscheet_data)
        query.save()


if __name__ == '__main__':
    put_db()