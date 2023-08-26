from . import mongo_db

def encrypt(name,email,password):
    key = "dummy"
    result = mongo_db.upsert(name,email,password,key)
    return result