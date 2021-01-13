import socket


def addr2b(addr):
	ip, port = addr
	return (ip+":"+str(port)).encode()

def b2addr(comb):
	des = comb.split(":")
	ip = des[0]
	port = int(des[1])
	return (ip, port) 


ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("server: created")

hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
port = 80
addrlist = []

ss.bind((host, port))
print("server: bound to", host, "on", port)

while True:
	data, addr = ss.recvfrom(4096)
	if data:
		print("request from: ", addr)
		addrlist.append(addr)
		if len(addrlist) >1:
			ss.sendto(addr2b(addrlist[0]), addrlist[1])
			ss.sendto(addr2b(addrlist[1]), addrlist[0])
			addrlist.pop()
			addrlist.pop()