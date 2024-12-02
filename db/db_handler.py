from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ia_database"]
collection = db["ia_data"]

def upsert_data(data):
    for item in data:
        collection.update_one(
            {"title": item["title"]},
            {"$set": item},
            upsert=True
        )

def get_all_data():
    return list(collection.find({}, {"_id": 0}))
