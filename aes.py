from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.hazmat.primitives import serialization

import base64
import hashlib
from Cryptodome.Cipher import AES




def encrypt_aes(key,message):
    message = message.encode()
    raw = pad(message)
    cipher = AES.new(key, AES.MODE_CBC,iv)
    enc = cipher.encrypt(raw)
    return base64.b64encode(enc).decode()

def decrypt_aes(key, enc):
    enc = base64.b64decode(enc)
    cipher = AES.new(key, AES.MODE_CBC,iv)
    dec = cipher.decrypt(enc)
    return unpad(dec).decode()


message = input()
print(f"입력한 메시지 : {message}\n")



x = 2048
y = 256
result = int((x/8)-(2*y/8)-2)

if(bytes(len(message)) < bytes(result)):
    print(result)
    message = message.encode()
    with open("private_key.pem","rb")as key_file: ##개인 키 
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
    )

    with open("public_key.pem","rb")as key_file: ## 공유키 
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
    )
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("\n암호문 :", encrypted)
    original_message = private_key.decrypt( 
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()), ##256 비트 
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    print("\n복호문 :", original_message)
    original_message = original_message.decode()

    print("\n처음 입력한 메시지 :", original_message)
else:
    
    block_size = 16
    pad = (lambda s: s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size).encode())
    unpad = (lambda s: s[:-ord(s[len(s)-1:])])
    
    key = '12345678912345678912345678912312'
    key = hashlib.sha256(key.encode()).digest()

    iv = bytes([0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x08,0x06,0x05,0x04,0x03,0x02,0x01])

    encrypt_aes = encrypt_aes(key,message)
    decrypt_aes = decrypt_aes(key,encrypt_aes)
      
    print(f"암호문 : {encrypt_aes}\n")

    print(f"복호문 : {decrypt_aes}\n")


