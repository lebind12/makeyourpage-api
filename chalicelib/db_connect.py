import pymongo
import os

from pymongo.mongo_client import MongoClient

def connection() :
    # local connection
    DB_DATABASE = 'dev'

    # deploy connection
    # DB_URI = os.environ.get("DB_URI")
    # DB_DATABASE = os.environ.get("DB_DATABASE")

    db = MongoClient(DB_URI, tls=True, tlsAllowInvalidCertificates=True)
    return db[DB_DATABASE]