from pymongo.mongo_client import MongoClient
import pymongo
import pymongo.errors
import encrypter
from random import randint
import datetime

uri = "mongodb+srv://awstestuser1998:awstestuser1998@cluster0.nb2lq1w.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection


def insert_into(username, email, password):
  try:
    db = client.cred
    table = db.auth_table
    db.auth_table.create_index([('email', pymongo.ASCENDING)], unique=True)
    result = encrypter.encrypt(password)
    key = result[1]
    decoded_password = result[0]
    query = {
        "username": username,
        "email": email,
        "password": decoded_password,
        "key": key
    }
    #print(query)
    table.insert_one(query)
    id = ''.join(str(randint(0, 10)) for x in range(4))
    #print("ID Created: ", id)
    tenant_id = id
    db_2 = client[id]
    table2 = db_2.accounts
    table2.insert_one({})
    table.update_one({"email": email}, {"$set": {"tenantid": tenant_id}})
    return "success"
  except TypeError as err:
    return err
  except pymongo.errors.DuplicateKeyError:
    return "Email ID {} already present, please use different ID to create".format(
        email)


# def add(username,appname,password):
