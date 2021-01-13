import socket
from threading import Thread
import time


def b2addr(comb):
	comb = comb.decode()
	des = comb.split(":")
	ip = des[0]
	port = int(des[1])
	return (ip, port) 


ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "192.168.0.10"
port = 80
saddr = (ip, port)

ss.sendto(b'0', (ip, port))
data, addr = ss.recvfrom(128)
print(data, addr)
addr = b2addr(data)


sending = Thread(target=ss.sendto, args=(b'0', addr))
sending.start()
data, addr = ss.recvfrom(128)
print(data, addr)
sending.join()