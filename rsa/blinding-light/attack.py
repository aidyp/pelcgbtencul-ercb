import codecs

host = "socket.cryptohack.org"
port = 13376
ADMIN_TOKEN = b"admin=True"

'''
Aim is to sign the ADMIN TOKEN.
The server code checks to see that you're not trying to sign the admin token

Solution is to get it to sign something that we have made that we can modify to make the admin token

Signing = m^d (N)
c = (a^2)^d = a^(2d) (N)
then c^(1/2) = a^(2d)^1/2 = a^d (N)
'''


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

def xor(a, b):
	'''
	xor two equally sized hex strings
	'''
	return "".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(a, b)])




