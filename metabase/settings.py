from metabase import Metabase
from os import environ
import yaml


def init():
    global metabase
    with open('metabase/secrets.yml') as f:
        data = yaml.safe_load(f)
        environ['METABASE_ENDPOINT'] = data['metabase_url']
        metabase = Metabase(
            email=data['metabase_credentials']['email'],
            password=data['metabase_credentials']['password']
        )
