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
    result = mongo_db.create_tenant(name,email,encrypted,key)
    return result

def decrypt(password,key):
    password = password
    key = key
    f = Fernet(key)
    decrypted_pass = f.decrypt(password)
    decrypted_pass = decrypted_pass.decode()
    return decrypted_pass