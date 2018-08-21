from pymongo import MongoClient
from neo4j.v1 import GraphDatabase
import os


MONGO_INITDB_ROOT_USERNAME = os.getenv('MONGO_INITDB_ROOT_USERNAME')
MONGO_INITDB_ROOT_PASSWORD = os.getenv('MONGO_INITDB_ROOT_PASSWORD')


# TODO - Should we rename this or put neo4j stuff in separate folder?
client = MongoClient(
    host='mongo', port=27017, username=MONGO_INITDB_ROOT_USERNAME,
    password=MONGO_INITDB_ROOT_USERNAME, authSource='admin'
)


# Mongo Collections
messages = client.test.messages
api_keys = client.test.api_keys