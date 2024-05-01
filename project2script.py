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

good_docs = 0
docs_not_imported = 0
corrupt_docs = 0


def check_json(json_data):
   try:
       # Attempt to load JSON data
       json.loads(json_data)
       return True
   except json.JSONDecodeError:
       # If JSON decoding fails, return False
       return False


for filename in os.listdir(directory):
   try:
       with open(os.path.join(directory, filename)) as f:
           new_data = json.load(f)
           good_docs+=len(new_data)
           collection = db[collection_name]
           collection.insert_many(new_data)
   except Exception as e:
        print(f"Error decoding JSON in file {filename}: {e}")
        with open(os.path.join(directory, filename)) as f:
           broken_file = f.read()
           documents = broken_file.strip("[").strip("]").split('"_id"')
           documents.pop(0)
           for i in documents:
                strip = i.strip(" ").strip("'").strip("{").strip(",")
                id_fixed = '{"_id"'+strip
                if id_fixed.endswith("}"):
                    docs_not_imported+=1
                else:
                   corrupt_docs+=1


              
print(docs_not_imported)
print(corrupt_docs)
print(good_docs)