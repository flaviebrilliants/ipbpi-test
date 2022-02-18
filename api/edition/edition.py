import json

from test import TestCase


class Editions(TestCase):
    def start(self):
        self.run(self.url, params=self.args)

    def check_resfields(self, response):
        data = json.loads(response.text)
        for item in data:
            temp_resfields = item.keys()
            for temp_resfield in temp_resfields:
                if temp_resfield in self.resfields:
                    continue
            return True


class EditionsVolumes(TestCase):
    def start(self):
        self.run(self.url, params=self.args)