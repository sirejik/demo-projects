import configparser

from elasticsearch import Elasticsearch

config = configparser.ConfigParser()
config.read('config.ini')

host = config.get('Elasticsearch', 'host')
port = config.get('Elasticsearch', 'port')

es = Elasticsearch([{'host': host, 'port': port}])
