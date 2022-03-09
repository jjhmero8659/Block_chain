import sys,os
from cryptography.fernet import Fernet

key = Fernet.generate_key() ##key 값 자동할당  
f = Fernet(key) 

file = open("data.txt","r") ##data.txt 파일 읽기 변환
encrypted_file = file.read() ##읽은 파일을 변수에 저장
file.close()

token = f.encrypt(encrypted_file.encode()) ##해당파일 암호화,stack_overflow

token = token.decode()

print(token) ##암호문 출력

file = open("encrypted.txt","w")    ##encrypted.txt 생성후 쓰기모드
file.write(token)         ##encrypted.txt 에 쓰기
file.close()

file = open("encrypted.txt","r")    ##복호화 한 파일을 읽기모드로 전환
decrypted_file = file.read().encode() ##파일을 읽어서 변수에 저장

result = f.decrypt(decrypted_file) ##암호문 복호화

print(result) ##값 출력

