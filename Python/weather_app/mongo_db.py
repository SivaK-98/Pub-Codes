import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://awstestuser1998:awstestuser1998@cluster0.nb2lq1w.mongodb.net/?retryWrites=true&w=majority"
)
db = client.weather
table = db.logging


def insert_entries(data):
  try:
    table.insert_one(data)
    return "successfully added entry to db"
  except:
    return "Error"
