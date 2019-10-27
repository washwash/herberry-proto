import click
from app import application
from herberry.medications.crawler import harvest_medications


(
    application.cli.
    command('harvest_medications')
    (click.argument('service_name')(harvest_medications))
)
