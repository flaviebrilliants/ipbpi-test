import logging

FORMAT = '%(message)s'
logging.basicConfig(filename='test.log', filemode='w', level=logging.INFO, format=FORMAT)
logger = logging.getLogger('ApiTest')
logger.addHandler(logging.StreamHandler())