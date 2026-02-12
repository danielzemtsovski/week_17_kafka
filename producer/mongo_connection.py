import json
from pymongo import MongoClient
from os import getenv


mongo_uri = getenv("MONGO_URI", "mongodb://root:root123@localhost:27017/")
mongo_db = getenv("MONGO_DB", "db")
mongo_collection = getenv("MONGO_COLLECTION", "collection")
file_path = './suspicious_customers_orders.json'

myclient = MongoClient(mongo_uri)

db = myclient[mongo_db]

collection = db[mongo_collection]

with open("suspicious_customers_orders.json") as file:
    file_data = json.load(file)


ins_result = collection.insert_many(file_data)












