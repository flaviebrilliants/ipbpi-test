import json

from logger import logger

from test import TestCase


class Bpas(TestCase):
    def start(self):
        self.run(self.url, params=self.args)

    def check_resfields(self, response):
        data = json.loads(response.text)
        for county in data:
            temp_resfields = county.items()
            return self._check(temp_resfields, self.resfields)

    # рекуссивный метод проверки полей
    def _check(self, temp_resfields, resfields=None):
        for key, value in temp_resfields:
            if isinstance(value, list):
                for element in value:
                    inside_resfields = resfields.get(key)
                    self._check(element.items(), inside_resfields)
            if key in resfields.keys():
                continue
            else:
                return False
        return True


class Classifiers(TestCase):
    def start(self):
        self.run(self.url, params=self.args)


class SearchBpa(TestCase):
    def start(self):
        self.run(self.url, params=self.args)

    def check_resfields(self, response):
        data = json.loads(response.text)
        return self._check(data.items(), self.resfields)

    # рекуссивный метод проверки полей
    def _check(self, temp_resfields, resfields=None):
        for key, value in temp_resfields:
            if isinstance(value, list):
                for element in value:
                    inside_resfields = resfields.get(key)
                    if inside_resfields is None:
                        continue
                    self._check(element.items(), inside_resfields)
            if key in resfields.keys():
                continue
            else:
                return False
        return True


class DocumentCard(TestCase):
    def start(self):
        self.run(self.url, params=self.args)

    def check_resfields(self, response):
        data = json.loads(response.text)
        return self._check(data.items(), self.resfields)

    # рекуссивный метод проверки полей
    def _check(self, temp_resfields, resfields=None):
        for key, value in temp_resfields:
            if isinstance(value, list):
                for element in value:
                    inside_resfields = resfields.get(key)
                    if inside_resfields is None:
                        continue
                    self._check(element.items(), inside_resfields)
            if key in resfields.keys():
                continue
            else:
                return False
        return True


class DocumentText(TestCase):
    def start(self):
        self.run(self.url, params=self.args)


class BpaDocumentFile(TestCase):
    def start(self):
        self.run(self.url, params=self.args)