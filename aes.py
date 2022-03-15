from cryptography.hazmat.primitives import serialization

pem = private_key.private_bytes(
    enconding = serialization.Encoding.PEM,
    format = serialization.PrivateFormat.PKCS8,
    encryption_algorithm = serialization.NoEncryption()
    )
with open('private_key.pem','wb')as f:
    f.write(pem)

## 개인 키를 파일에 저장

with open("private_key.pem","rb")as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
##파일에 저장된 개인 키를 읽어오기

pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open('public_key.pem','wb')as f:
    f.write(pem)
##공개 키를 파일에 저장

with open("public_key.pem","rb")as key_file:
    publick_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

#파일에 저장된 공개 키를 읽어오기
