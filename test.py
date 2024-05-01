from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json


MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.testing
# specify a collection




directory = "data"


collection_name ="json_data"
filename="generated00.json"

try:
    with open(os.path.join(directory, filename)) as f:
        new_data = json.load(f)
        collection = db[collection_name]
        collection.insert_many(new_data)
except Exception as e:
        print(f"Error decoding JSON in file {filename}: {e}")