import socket
from threading import Thread
import time

def b2addr(comb):
	comb = comb.decode()
	des = comb.split(":")
	ip = des[0]
	port = int(des[1])
	return (ip, port) 


def pingudp(socket, addr):
	for i in range(50):
		print("sending ping to ", addr)
		socket.sendto("ping".encode(), addr)
		time.sleep(1)



ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "1.248.169.25"
port = 80
saddr = (ip, port)


ss.sendto(b'0', (ip, port))
data, addr = ss.recvfrom(128)
addr = b2addr(data)
print(addr)


sending = Thread(target=pingudp, args=(ss, addr))
sending.start()
data, addr = ss.recvfrom(128)
print(data, addr)
sending.join()
