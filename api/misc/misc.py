from test import TestCase


class DocumentCounter(TestCase):
    def start(self):
        self.run(self.url, self.args)