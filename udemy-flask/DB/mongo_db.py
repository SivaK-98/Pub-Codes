import pymongo
import pymongo.errors
from . import enc_dec
from random import randint
import datetime

client = pymongo.MongoClient("mongodb://4.247.163.207:27017/")
db = client.vault
table = db.auth_db
db.auth_db.create_index([('email',pymongo.ASCENDING)],unique=True)

def create_tenant(name,email,password,key):
    data = {}
    data["name"] = name
    data["email"] = email
    data["password"] = password
    data["key"] = key
    try:
        table.insert_one(data)
        id = ''.join(str(randint(0,10)) for x in range(4))
        print("ID Created: ",id)
        tenant_id = id
        db_2 = client[id]
        table2 = db_2.created_time
        table2.insert_one({"created":str(datetime.datetime.now())})
        print(db_2)
        table.update_one({"email":email},{"$set":{"tenantid":tenant_id}})
        return "ID Created"

    except TypeError as err:
        return err
    except pymongo.errors.DuplicateKeyError:
        return "Email ID {} already present, please use different ID to create".format(email)
    
def validate(email,password):
    data = {}
    data["email"] = email
    password = password
    key = "dummy"
    #table.find_one(data)
    result = enc_dec.decrypt(password,key)
    return result


# Completed till avoiding duplicate entries.
# Need to create login feature.