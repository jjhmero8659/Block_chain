#!/usr/bin/env python3

import socket

host = 'localhost'
port = 12345

sock = socket.socket((socket.AF_INET, socket.SOCK_DGRAM , socket.IPPROTO_UDP))
sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR,1 )

sock.bind((host,port))

# print(sock)
(data, address) = sock.recvfrom(65565)
print(f"received {len(data)} bytes from {address}")

sock.close()