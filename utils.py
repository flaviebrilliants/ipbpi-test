from config import user
from config import password

import json

import requests

import config


def get_token():
    r = requests.post('http://{}/api/personal/auth.json?login={}&password={}'.format(config.WEB_DOMAIN, user, password))
    data = json.loads(r.text)
    return data['token']