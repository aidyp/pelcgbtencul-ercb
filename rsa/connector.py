import socket
import json


def netcat(host, port, content):
	'''
	Code to send/receive data from the TCP socket
	'''
	ret = []
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port)))
	s.sendall(content.encode())
	s.shutdown(socket.SHUT_WR)
	while True:
		data = s.recv(4096)
		if not data:
			break
		ret.append(data)
	s.close()
	return ret

def to_json(data):
	'''
	Add some error checking 
	'''
	try:
		temp = data[1].decode('utf-8')
		temp = temp.split('\n')
		return json.loads(temp[0])
	except IndexError:
		return -1
