import json

import requests
import time
from logger import logger
from urllib.parse import unquote


class TestCase:
    def __init__(self, name, method, url, args, resfields):
        self.name = name
        self.method = method
        self.url = url
        self.args = args
        self.resfields = resfields

        self.start()

    # виртуальный метод старта
    def start(self):
        raise NotImplementedError

    # обработка
    def run(self, query, params=None):
        logger.info('Тестирование: {}'.format(self.name))
        response = self.call(query, params, self.method)
        self.check(response)

    # вызов api метода
    def call(self, query, params, method):
        if method == 'GET':
            r = requests.get(query, params=params)
            logger.info('\tURL: {}'.format(unquote(r.url)))
        if method == 'POST':
            r = requests.post(query, params=params)
            logger.info('\tURL: {}'.format(unquote(r.url)))
        return r

    # метод проверки (серия микро-тестов)
    def check(self, response):
        check_code200 = self.check_200response(response)
        logger.info('\tДозвонились? - {}'.format(check_code200))

        if self.resfields is not None:
            check_resfields = self.check_resfields(response)
            logger.info('\tПоля на месте? - {}'.format(check_resfields))

    # сервер не отвечает, а кто звонит?
    def check_200response(self, response):
        if response.status_code == 200:
            return True
        else:
            return False

    # проверка результирующих полей в ответе
    def check_resfields(self, response):
        data = json.loads(response.text)
        temp_resfields = data.keys()
        for temp_resfield in temp_resfields:
            if temp_resfield in self.resfields:
                continue
        return True