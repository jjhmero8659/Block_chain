import socket
import sys

target_host = sys.argv[1]

for port in range(0,1024): #0~1023 까지 반복
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    check = s.getsockname()
    
    try:
        result = s.connect_ex( (target_host,port) ) # true : return == 0 , false : return == 111
        if result == 0:
            print(f"Port {port} open")
    except:
        pass
    
    s.close()