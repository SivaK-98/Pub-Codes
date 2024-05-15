from cryptography.fernet import Fernet


def encrypt(password):
  key = Fernet.generate_key()
  f = Fernet(key)
  password = password.encode()
  message = f.encrypt(password)
  decoded = message.decode()
  key = key.decode()
  return decoded,key
  