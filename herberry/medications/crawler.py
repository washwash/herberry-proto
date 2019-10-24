import logging

from app import mongo

logging.basicConfig(
    filename='harvest_medications.log',
    level=logging.INFO
)


def harvest_medications(path):
    mongo.db
    from ipdb import set_trace;set_trace()
    logging.info(f'harvest {path}')
