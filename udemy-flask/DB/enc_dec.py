from . import mongo_db
from cryptography.fernet import Fernet 

def encrypt(name,email,password):
    print(name)
    print(email)
    print(password)
    key = Fernet.generate_key()
    print(key.decode())
    f = Fernet(key)
    encrypted = f.encrypt(password.encode()).decode()
    print(encrypted)
    result = mongo_db.upsert(name,email,encrypted,key)
    return result

def decrypt(password,key):
    password = password
    key = key
    return "login success"