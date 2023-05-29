import pymongo
import enc_dec
from datetime import datetime
from pymongo.errors import CollectionInvalid, InvalidName, DuplicateKeyError

date = datetime.now()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["vault"]
mycol = mydb["users"]
mycol.create_index([('username', pymongo.ASCENDING)], unique=True)


def signup(username, password, email, mobile):
    key, enc_pass = enc_dec.encrypt_pass(password)
    # print(key.decode())
    # print(enc_pass.decode())
    query = {"username": username, "password": enc_pass.decode(), "key": key.decode(), "email": email, "mobile": mobile,
             "created": date}
    try:
        x = mycol.insert_one(query)
        db = myclient[username]
        mycoll2 = db["creds"]
        mycoll2.create_index([('username', pymongo.ASCENDING)], unique=True)
        test = mycoll2.insert_one({"appname": "testapp", "appuser": "testuser", "apppass": "testpass", "created": date})
        return f"Account created successfully for the user {username}"
    except InvalidName:
        return "No user name specified"
    except DuplicateKeyError:
        return "Username already taken, please use unique username"


def login(username, password):
    try:
        x = mycol.find_one({"username": username})
        print(x)
        key = x["key"]
        enc_pass = x["password"]
        dec_pass = enc_dec.decrypt_pass(enc_pass, key).decode()
        print("decrypted pass: ", dec_pass)
        if dec_pass == password:
            return "Login Success"
        else:
            return "password incorrect"
    except TypeError:
        return "Username Not found"
