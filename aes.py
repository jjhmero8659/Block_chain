from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from cryptography.hazmat.primitives import serialization

message = input()
print("입력한 메시지 :" , message)
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
print("")
print("암호문 :", encrypted)

original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
print("")
original_message = original_message.decode()
print("복호문 :", original_message)

    


##private_key = rsa.generate_private_key(
##    public_exponent=65537,
##    key_size=2048,
##    backend=default_backend()
##)
##
##public_key = private_key.public_key() ## rsa 공개키 생성
##
##print(public_key)
##
##encrypted = public_key.encrypt(
##    message,
##    padding.OAEP(
##        mgf=padding.MGF1(algorithm=hashes.SHA256()),
##        algorithm=hashes.SHA256(),
##        label=None
##    )
##)
##print("")
##print(encrypted)

##pem = private_key.private_bytes(
##    enconding = serialization.Encoding.PEM,
##    format = serialization.PrivateFormat.PKCS8,
##    encryption_algorithm = serialization.NoEncryption()
##    )
##with open('private_key.pem','wb')as f:
##    f.write(pem)
#### 개인 키를 파일에 저장
##
##with open("private_key.pem","rb")as key_file:
##    private_key = serialization.load_pem_private_key(
##        key_file.read(),
##        password=None,
##        backend=default_backend()
##    )
####파일에 저장된 개인 키를 읽어오기
##
##pem = public_key.public_bytes(
##    encoding=serialization.Encoding.PEM,
##    format=serialization.PublicFormat.SubjectPublicKeyInfo
##)
##
##with open('public_key.pem','wb')as f:
##    f.write(pem)
####공개 키를 파일에 저장
##
##with open("public_key.pem","rb")as key_file:
##    publick_key = serialization.load_pem_public_key(
##        key_file.read(),
##        backend=default_backend()
##        )
####파일에 저장된 개인 키를 읽어오기 

##
### #파일에 저장된 공개 키를 읽어오기
##
