import json
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://charlie:Vurxac123!@qra-408sample-721gh.gcp.mongodb.net/test?retrywrites=true&w=majority")
db = client['QRA']
trader = db['Trader']
#db = client['QRA-408sample']
#db.createCollection("CollectionName")
#input_file = open("input_file.json", "r")


with open("input_file.json") as f:
    file_data = json.load(f)
    print(file_data)
    trader.insert_one(file_data)

