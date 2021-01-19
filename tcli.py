import socket
from threading import Thread
import time
import select


def b2addr(comb):
	comb = comb.decode()
	des = comb.split(":")
	ip = des[0]
	port = int(des[1])
	return (ip, port) 


def pingudp(socket, addr):
	for i in range(50):
		socket.sendto("ping".encode(), addr)
		time.sleep(150)

def initialping(socket, addr):
	for i in range(50):
		socket.sendto("ping".encode(), addr)
		time.sleep(1)

def get_initialping(socket):
	pass


ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "192.168.0.10"
port = 80
saddr = (ip, port)

print("request to ", (ip, port))
ss.sendto(b'0', (ip, port))
data, addr = ss.recvfrom(128)
addr = b2addr(data)
print(addr)


sending = Thread(target=initialping, args=(ss, addr))
sending.start()
data, addr = ss.recvfrom(128)
print(data, addr)
sending.join()
