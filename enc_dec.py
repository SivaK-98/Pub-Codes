from cryptography.fernet import Fernet, MultiFernet


def encrypt_pass(password):
    key = Fernet.generate_key()
    f = Fernet(key)
    encoded_pass = password.encode()
    encrypted_pass = f.encrypt(encoded_pass)
    # print("from enc_dec", encrypted_pass.decode())
    # print("from enc_dec", key.decode())
    return key, encrypted_pass


def decrypt_pass(password, key):
    f = Fernet(key)
    # print(password)
    decMessage = f.decrypt(password)
    return decMessage
