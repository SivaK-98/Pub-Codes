import pymongo

client = pymongo.MongoClient("mongodb://4.247.163.207:27017/")
db = client.weather
table = db.logging


def insert_entries(data):
    try:
        table.insert_one(data)
        return "successfully added entry to db"
    except:
        return "Error"
