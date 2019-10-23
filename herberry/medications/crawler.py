import logging


logging.basicConfig(
    filename='harvest_medications.log',
    level=logging.INFO
)


def harvest_medications(path):
    logging.info(f'harvest {path}')
