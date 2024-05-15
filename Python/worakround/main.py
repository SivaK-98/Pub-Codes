import os
import pandas as pd
import pymongo
from decimal import *
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://awstestuser1998:awstestuser1998@cluster0.nb2lq1w.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
table_data = []

db = client["airbnb"]
table = db["airbnb_data"]
query = {"_id": 0, "beds": 1, "price": 1, "images.picture_url": 1}
# Send a ping to confirm a successful connection
try:
  client.admin.command('ping')
  print("Pinged your deployment. You successfully connected to MongoDB!")
  data = table.find({}, query)
  for value in data:
    print(value)
    temp_data = []
    beds = value['beds']
    price = value['price']
    images = value['images']['picture_url']
    temp_data.append(beds)
    temp_data.append(price)
    temp_data.append(images)
    table_data.append(temp_data)
    #print(temp_data)
  #print(table_data)
  df = pd.DataFrame(table_data, columns=['Beds', 'Price', 'Image'])
  print(df)
  df.to_html("templates/mongo_data.html")
except Exception as e:
  print(e)
  pass
