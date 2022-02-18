import utils
from test import TestCase


class Auth(TestCase):
    def start(self):
        self.run(self.url, params=self.args)


class UpdateToken(TestCase):
    def start(self):
        self.args['token'] = utils.get_token()
        self.run(self.url, params=self.args)


class UpgradeToken(TestCase):
    def start(self):
        self.args['token'] = utils.get_token()
        self.run(self.url, params=self.args)


class LogOut(TestCase):
    def start(self):
        self.args['token'] = utils.get_token()
        self.run(self.url, params=self.args)


class CheckToken(TestCase):
    def start(self):
        self.args['token'] = utils.get_token()
        self.run(self.url, params=self.args)


class ConfigList(TestCase):
    def start(self):
        self.args['token'] = utils.get_token()
        self.run(self.url, params=self.args)


class Config(TestCase):
    def start(self):
        self.args['token'] = utils.get_token()
        self.run(self.url, params=self.args)


class UserGet(TestCase):
    def start(self):
        self.args['token'] = utils.get_token()
        self.run(self.url, params=self.args)
