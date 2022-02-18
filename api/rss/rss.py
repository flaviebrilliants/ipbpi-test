import json

import requests

from test import TestCase


class BPAsList(TestCase):
    def start(self):
        self.run(self.url, params=self.args)


class RSSClassifiers(TestCase):
    def start(self):
        self.run(self.url, params=self.args)


class RSSGeneratorFeed(TestCase):
    def start(self):
        self.run(self.url, params=self.args)
