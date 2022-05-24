import os

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

from sheetapi.settings import ADD_PATH, SCOPES, CODE_SHEET, RANGES


def get_service_canalserice():
    """
    Могу читать и (возможно) писать в таблицы кот. выдан доступ
    для сервисного аккаунта приложения
    canal-service@canalservice-v2.iam.gserviceaccount.com
    :return:
    """
    creds_json = os.path.dirname(__file__) + ADD_PATH
    scopes = SCOPES

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


def get_sheet():
    """
    Возвращаем с Google sheet данные из Лист1
    :return: данные в json неочищенные
    """
    service = get_service_canalserice()
    sheet = service.spreadsheets()

    # https://docs.google.com/spreadsheets/d/xxx/edit#gid=0

    # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchGet
    resp = sheet.values().batchGet(spreadsheetId=CODE_SHEET, ranges=RANGES).execute()
    return resp.get('valueRanges')[0].get('values')
