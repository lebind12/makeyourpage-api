import json
import os
from pymongo.mongo_client import MongoClient

def connection() :
    json_file = open(os.getcwd()+ '/chalicelib/environment.json', 'r')
    json_data = json.load(json_file)
    # local connection
    DB_URI = json_data['DB_URI']
    DB_DATABASE = json_data['DB_DATABASE']

    db = MongoClient(DB_URI, tls=True, tlsAllowInvalidCertificates=True)
    json_file.close()
    return db[DB_DATABASE]