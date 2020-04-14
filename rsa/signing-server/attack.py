import socket
import json

host = "socket.cryptohack.org"
port = 13374
import codecs

'''
RSA signing is exponentiation with the private key, d
sign(x) = x^d (N)

We get the encrypted message c
c = m^e (N)

Then "sign" the message
sign(c) = c^d = m^e^d = m^ed = m (N)          | By definition of RSA
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


def get_pubkey():
	'''
	Gets the public key as a dictionary with two integers
	'''
	content = '{\"option\":\"get_pubkey\"}'
	data = netcat(host, port, content)
	proc = to_json(data)
	proc['N'] = int(proc['N'][2:], 16)
	proc['e'] = int(proc['e'][2:], 16)
	return proc

def get_secret():
	'''
	Gets the secret as a hex string, recall c = m^e (N)
	'''
	content = '{\"option\":\"get_secret\"}'
	data = netcat(host, port, content)
	proc = to_json(data)
	proc['secret'] = proc['secret'][2:]
	return proc
	

def sign_data(content):
	'''
	Recall m = c^d (N), and signing is raising to the power of the secret key
	Passes in the content as a json
	'''
	data = netcat(host, port, content)
	proc = to_json(data)
	return proc

def repack_secret(secret):
	package = {'option':'sign', 'msg':secret['secret']}
	package = str(package).replace("\'", "\"")
	return package
	
def to_chr(hex_string):
	decode_hex = codecs.getdecoder("hex_codec")
	return decode_hex(hex_string)[0]
	

def attack():
	secret = get_secret()
	to_sign = repack_secret(secret)
	signed = sign_data(to_sign)
	signed = signed['signature'][2:]
	print(to_chr(signed))

attack()
