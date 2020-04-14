import codecs
import math
import socket
import json
from decimal import *
host = "socket.cryptohack.org"
port = 13376
ADMIN_TOKEN = b"admin=True"

'''
Aim is to sign the ADMIN TOKEN.
The server code checks to see that you're not trying to sign the admin token

If the admin token is a, we want a^d (N)

Solution is to get it to sign something that we have made that we can modify to make the admin token

Signing = m^d (N)
(1) compute (a * b), let b = 2, a = admin token
(2) sign (a * b) = (a * b)^d = a^d * b^d (N)
(3) sign (b) = b^d (N)
(4) Compute the modular inverse of b^d, c, such that (b^d) * c == 1 (N)
(5) Multiply (2) by (4) = (a * b)^d * c = a^d * (b^d * c) = a^d (N)
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

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def blind_token():
	hex_token = ADMIN_TOKEN.hex()
	temp = int(hex_token, 16)
	temp = temp * 2
	blinded = hex(temp)[2:]
	return blinded

def unblind_token(signature, n):
	'''
	Get the signature for just 2
	'''
	hex_blind = '02'
	blind_sign = sign_token(hex_blind)
	blind_int = int(blind_sign, 16)
	# Cheated and used SAGE to find modular inverse, should find the python libraries to do so!
	inv =9862019620971741369116087109955192146872628895464633384803798439261336448638202674486411183716810752822401121256819700685521262811469417624137111408818819977689976502566484723962311725081220015699435749414212165810619768070353750141754835616744086704023757901133283892655625111798416970047252092108573464514556340189976760936508838315585104796199773748924598335707382525339483666793044108904479029009193117634075933955236576323280288961415457246621942269538236498997266335872788393330564776870690317792008551685897918984158282778725304977565396518324675526830056967602408839913864240243995543496219273253082264720119
	sig_int = int(signature, 16)
	admin_int = (sig_int * inv) % n
	return hex(admin_int)[2:]
	

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


def to_chr(hex_string):
	decode_hex = codecs.getdecoder("hex_codec")
	return decode_hex(hex_string)[0]

def sign_token(hex_token):
	'''
	Signs a token, returns the signed value
	'''
	content = {'option':'sign', 'msg':hex_token}
	content = str(content).replace('\'', '\"')
	data = netcat(host, port, content)
	result_json = to_json(data)
	signature = result_json['signature'][2:]
	return signature

def get_pubkey():
	'''
	Gets the public key as a dictionary with two integers
	'''
	content = '{\"option\":\"get_pubkey\"}'
	data = netcat(host, port, content)
	proc = to_json(data)
	proc['N'] = int(proc['N'][2:], 16)
	proc['e'] = int(proc['e'][2:], 16)
	return proc['N']

def verify_token(hex_token):
	'''
	Tries to verify a token
	'''
	content = {'option':'verify', 'msg':ADMIN_TOKEN.hex(), 'signature':hex_token}
	content = str(content).replace('\'', '\"')
	data = netcat(host, port, content)
	result_json = to_json(data)
	print(result_json)

n = get_pubkey()
print(n)
blinded = blind_token()
signature = sign_token(blinded)
unblinded = unblind_token(signature, n)
verify_token(unblinded)


