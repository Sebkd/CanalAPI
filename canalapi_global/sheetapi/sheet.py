import os
from pprint import pprint

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# from canalapi_global.sheetapi.models import Sheet
from sheetapi.settings import RANGES, SCOPES, ADD_PATH, CODE_SHEET


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
    # service = get_service_simple()
    service = get_service_canalserice()
    sheet = service.spreadsheets()

    # https://docs.google.com/spreadsheets/d/xxx/edit#gid=0
    # https://docs.google.com/spreadsheets/d/1XQanaCg8lqBG1tt4pY0A1jYLJfL0cLDNft0AFkhd4wg/edit#gid=0

    # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get
    # resp = sheet.values().get(spreadsheetId=sheet_id, range="Лист1!A1:A999").execute()

    # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchGet
    resp = sheet.values().batchGet(spreadsheetId=CODE_SHEET, ranges=RANGES).execute()
    return resp.get('valueRanges')[0].get('values')


if __name__ == '__main__':
    # service = get_service_simple()
    service = get_service_canalserice()
    sheet = service.spreadsheets()

    # https://docs.google.com/spreadsheets/d/xxx/edit#gid=0
    sheet_id = "1XQanaCg8lqBG1tt4pY0A1jYLJfL0cLDNft0AFkhd4wg"

    # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get
    # resp = sheet.values().get(spreadsheetId=sheet_id, range="Лист1!A1:A999").execute()

    # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchGet
    resp = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["Лист1"]).execute()

    pprint(resp)
    print()
    #
    # data = resp.get('valueRanges')[0].get('values')
    # query = Sheet.delete.all()
    # query.execute()
    # for line in data[1:]:
    #     query = Sheet(
    #         {'number': int(line[0]),
    #          'order': line[1],
    #          'cost_dollars': line[2],
    #          'delivery_time': line[3]})
