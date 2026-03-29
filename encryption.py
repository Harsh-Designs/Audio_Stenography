import os
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def load_key():
    # Create key if not exists
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

    # Read key
    with open(KEY_FILE, "rb") as f:
        key = f.read()

    # DEBUG (optional)
    # print("Key:", key, "Length:", len(key))

    return key

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(encrypted_msg):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_msg).decode()