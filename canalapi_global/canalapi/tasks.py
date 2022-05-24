import requests
from celery import app

from sheetapi.settings import TOKEN, CHANNEL_ID


@app.shared_task
def send_telegram_bot(text: str):
    """
    Отправка сообщения телеграм-ботом
    :param text: текст
    :return: удалось/не удалось
    """
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
        print("post_text error")
        return False
    else:
        print("post_text succes")
        return True
