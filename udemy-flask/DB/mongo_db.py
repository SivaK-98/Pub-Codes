import pymongo
from . import enc_dec
from random import randint

client = pymongo.MongoClient("localhost",27017)
db = client.vault
table = db.auth_db

def upsert(name,email,password,key):
    data = {}
    data["name"] = name
    data["email"] = email
    data["password"] = password
    data["key"] = key
    try:
        table.insert_one(data)
        id = ''.join(str(randint(0,10)) for x in range(4    ))
        print("ID Created: ",id)
        # To create a DB in the name of ID
        tenant_db = client.{}.format(id)
        tenant_db.test.insert_one({"Name":"test","user":"test"})
        return "account created"

    except TypeError as err:
        return err
def validate(email,password):
    data = {}
    data["email"] = email
    password = password
    key = "dummy"
    #table.find_one(data)
    result = enc_dec.decrypt(password,key)
    return result