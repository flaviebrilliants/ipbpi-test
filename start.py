import json
import os

from api.edition.edition import Editions, EditionsVolumes
from config import WEBSERVER_API_DIR as WEBSERVER_API_DIR, WEB_DOMAIN as WEB_DOMAIN
from api.bpa.bpa import Bpas, Classifiers, SearchBpa, DocumentCard, DocumentText
from api.misc.misc import DocumentCounter
from api.personal.personal import Auth, UpdateToken, UpgradeToken, LogOut, CheckToken, ConfigList, Config, UserGet
from logger import logger

from api.rss.rss import BPAsList, RSSClassifiers, RSSGeneratorFeed


class Starter:
    def __init__(self):
        self.apidir = WEBSERVER_API_DIR
        self.start()

    def _parse(self, data):
        name = data['name']
        method = data['method']
        url = 'http://' + WEB_DOMAIN + data['url']
        args = data['args']
        resfields = data['resfields']

        return name, method, url, args, resfields

    def _get_tests(self, path):
        with open(path) as fo:
            data = json.load(fo)
            return data

    def _runner(self, dirpath, file, invoke):
        tests = self._get_tests(os.path.join(os.getcwd(), dirpath, file))
        for test in tests:
            try:
                name, method, url, args, resfields = self._parse(test)
                apitest = invoke(name, method, url, args, resfields)
            except Exception:
                logger.info('!!! Ошибка при тестировании API функции «{}»'.format(file))
                continue

    def start(self):
        for dirpath, dirnames, filenames in os.walk(WEBSERVER_API_DIR):
            try:
                if dirpath == 'api/rss':
                    logger.info('Тестирование api/rss')
                    for file in filenames:
                        if file == '01_bpas_list_view.json':
                            self._runner(dirpath, file, BPAsList)
                        if file == '02_rss_classifier_view.json':
                            self._runner(dirpath, file, RSSClassifiers)
                        if file == '03_feed_view.json':
                            self._runner(dirpath, file, RSSGeneratorFeed)
                if dirpath == 'api/misc':
                    logger.info('Тестирование api/misc')
                    for file in filenames:
                        if file == 'document_counter.json':
                            self._runner(dirpath, file, DocumentCounter)
                        if file == 'ipbpi_version.json':
                            raise ApiError(file)
                if dirpath == 'api/personal':
                    logger.info('Тестирование api/personal')
                    for file in filenames:
                        if file == '01_auth.json':
                            self._runner(dirpath, file, Auth)
                        if file == '02_update.json':
                            self._runner(dirpath, file, UpdateToken)
                        if file == '03_upgrade.json':
                            self._runner(dirpath, file, UpgradeToken)
                        if file == '04_logout.json':
                            self._runner(dirpath, file, LogOut)
                        if file == '05_check_token.json':
                            self._runner(dirpath, file, CheckToken)
                        if file == '06_config_list.json':
                            self._runner(dirpath, file, ConfigList)
                        if file == '07_config.json':
                            self._runner(dirpath, file, Config)
                        if file == '08_user.json':
                            self._runner(dirpath, file, UserGet)
                if dirpath == 'api/bpa':
                    logger.info('Тестирование api/bpa')
                    for file in filenames:
                        if file == '01_bpas.json':
                            self._runner(dirpath, file, Bpas)
                        if file == '02_bpa_classifier.json':
                            self._runner(dirpath, file, Classifiers)
                        if file == '03_bpa_search.json':
                            self._runner(dirpath, file, SearchBpa)
                        if file == '04_bpa_search_counter.json':
                            raise ApiError(file)
                        if file == '05_bpa_common_search.json':
                            raise ApiError(file)
                        if file == '06_bpa_document_card.json':
                            self._runner(dirpath, file, DocumentCard)
                        if file == '07_bpa_document_text.json':
                            self._runner(dirpath, file, DocumentText)
                        if file == '08_bpa_document_file.json':
                            raise ApiError(file)
                        if file == '09_bpa_document_content.json':
                            raise ApiError(file)
                        if file == '10_bpa_changes.json':
                            raise ApiError(file)
                if dirpath == 'api/edition':
                    logger.info('Тестирование api/edition')
                    for file in filenames:
                        if file == '01_editions.json':
                            self._runner(dirpath, file, Editions)
                        if file == '02_volumes.json':
                            self._runner(dirpath, file, EditionsVolumes)
                        if file == '03_divisions.json':
                            raise ApiError
                        if file == '04_edition_document_card.json':
                            raise ApiError
                        if file == '05_edition_document.json':
                            raise ApiError
            except ApiError as e:
                logger.info('Ошибка при тестировании api функции: {}'.format(e))
                continue


class ApiError(Exception):
    pass


if __name__ == '__main__':
    starter = Starter()
