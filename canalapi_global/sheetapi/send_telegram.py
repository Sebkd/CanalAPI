import datetime

import requests
from django.db.models import Q

from canalapi_global.sheetapi.models import Spreadscheet
from canalapi_global.sheetapi.settings import CHANNEL_ID, TOKEN


def send_telegram(text: str):
    token = TOKEN
    url = "https://api.telegram.org/bot"
    channel_id = CHANNEL_ID
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == '__main__':
    send_telegram("hello world!")
