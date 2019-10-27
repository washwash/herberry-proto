import logging
import string
from csv import DictReader
from itertools import chain

import scrapy
from scrapy.crawler import CrawlerProcess

from herberry.medications.models import Medication

logging.basicConfig(
    filename='harvest_medications.log',
    level=logging.INFO
)


class DrugsSpider(scrapy.Spider):
    name = 'drugs.com'

    @property
    def start_urls(self):
        url_base = 'https://www.drugs.com/alpha/{}.html'
        alphabet = string.ascii_lowercase
        letters = chain(
            *[
                [first_letter + second_letter for second_letter in alphabet]
                for first_letter in alphabet
            ]
        )
        return [url_base.format(letter) for letter in letters]

    def parse(self, response):
        for li in response.css('ul.ddc-list-column-2 li'):
            yield {
                'name': li.css('a::text').get(),
                'href': li.css('a')[0].attrib['href']
            }


class DrugsComHarvestService:
    data_url = '/tmp/herberry/meds'
    data_format = 'csv'
    throttling_delay = 0.5

    def __init__(self):
        self.harvester = DrugsSpider
        self.crawler_process = CrawlerProcess({
            'FEED_FORMAT': self.data_format,
            'FEED_URI': self.data_url,
            'DOWNLOAD_DELAY': self.throttling_delay
        })

    def collect_data(self):
        self.crawler_process.crawl(self.harvester)
        self.crawler_process.start()

    def save(self):
        with open(self.data_url, 'r') as f:
            reader = DictReader(f)
            for record in reader:
                Medication.save(record)


HARVEST_SERVICES = {
    'drugs.com': DrugsComHarvestService
}


def harvest_medications(service_name):
    logging.info(f'harvest {service_name}')

    service = HARVEST_SERVICES[service_name]()
    service.collect_data()
    service.save()

    logging.info(f'data from {service_name} was successfully harvested!')
