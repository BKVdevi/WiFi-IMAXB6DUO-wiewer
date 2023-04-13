import socket
from sre_parse import HEXDIGITS
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.102.42'
port = 20
while(s.connect_ex((host, port)) != 0):
    print("waiting...")
print("connected")
ds = 40000
fl = open("log.txt", "w");
while(ds > 0):
    a = s.recv(1)
    b = int.from_bytes( a, byteorder='big', signed=False )
    print(hex(b))
    fl.write(hex(b))
    fl.write(' ')
    ds -= 1;
s.close()
fl.close()
