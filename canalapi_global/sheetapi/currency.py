from pprint import pprint

import requests
import xml.etree.ElementTree as ET

from canalapi.sheetapi.settings import HEADERS, URL_CBR, CURRENCY


def get_currency(url=URL_CBR, headers=HEADERS, currency=CURRENCY):
    response = requests.get(url, headers=headers)
    doc = ET.fromstring(response.text)
    for element in tuple(doc.iter()):
        if element.attrib.get('ID') == currency:
            for elem in tuple(element.iter()):
                if elem.tag == 'Value':
                    return elem.text


if __name__ == '__main__':
    url_cbrf = URL_CBR
    headers = HEADERS
    currency = CURRENCY
    print(get_currency(url=url_cbrf, headers=headers, currency=CURRENCY))
