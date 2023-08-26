import pymongo

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
        return "account created"
    except TypeError as err:
        return err
    