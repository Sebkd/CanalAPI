"""
Необходимые константы для работы собирателя данных из google-sheet
"""
# данные для google-sheet
ADD_PATH = "/static/creds/canalservice-v2-73c9e10270bc.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# https://docs.google.com/spreadsheets/d/xxx/edit#gid=0
# https://docs.google.com/spreadsheets/d/1XQanaCg8lqBG1tt4pY0A1jYLJfL0cLDNft0AFkhd4wg/edit#gid=0
CODE_SHEET = "1XQanaCg8lqBG1tt4pY0A1jYLJfL0cLDNft0AFkhd4wg"
RANGES = ["Лист1"]

# данные для парсинга валюты
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 '
                             'Safari/537.36'}
URL_CBR = 'http://www.cbr.ru/scripts/XML_daily.asp'
CURRENCY = 'R01235'

# данные для телеграм-бот
"""ТУТ_ВАШ_ТОКЕН_КОТОРЫЙ_ВЫДАЛ_BotFather"""
TOKEN = '5259227325:AAH3aoFTv-AlvvxtNTzkv0L3x1uQ33zQf4A'
"""@ИМЯ_КАНАЛА"""
CHANNEL_ID = '@AndyGreyhound'
