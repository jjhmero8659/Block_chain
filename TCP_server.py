#!/usr/bin/env python3

import socket


host="127.0.0.1"
port = 12345

parent = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
parent.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
parent.bind( (host,port) )

parent.listen(10) #10대의 클라이언트 접속 허용

(child ,address) = parent.accept()  #client 접속할때 마다 child가 추가생성

# print("SERVER:parent",parent)
# print("SERVER:child",child)

# (data ,address) = child.recvfrom(65565) #client 접속할때 마다 child가 추가생성
(data) = child.recv(65565) #client 접속할때 마다 child가 추가생성 , address의 return이 없다 handshaking을 통한 상대방을 알기 때문
print(f"received {len(data)} bytes from {address}")

child.close()
parent.close()


