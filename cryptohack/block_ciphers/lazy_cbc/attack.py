import requests
import codecs
import time
from textwrap import wrap


def oracle_encrypt(plaintext):
	base_url = 'https://aes.cryptohack.org/lazy_cbc/encrypt/'
	ping_url = base_url + plaintext + '/'
	r = requests.get(ping_url)
	return r.json()['ciphertext']

def oracle_decrypt(ciphertext):
	base_url = 'https://aes.cryptohack.org/lazy_cbc/receive/'
	ping_url = base_url + ciphertext + '/'
	r = requests.get(ping_url)
	return r

def get_flag(key):
	base_url = 'https://aes.cryptohack.org/lazy_cbc/get_flag/'
	ping_url = base_url + key + '/'
	r = requests.get(ping_url)
	return r

def to_chr(hex_string):
	return "".join([chr(int(x, 16)) for x in hex_string])

	
def xor(a, b):
	'''
	xor two equally sized hex strings
	'''
	return "".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(a, b)])

def test_bad_ascii(hex_string):
	'''
	Want an ascii string that is guaranteed to break
	'''
	
	try:
		bytes.fromhex(hex_string).decode('ascii')
	except UnicodeDecodeError:
		print("Success")
		return
	print("Failure")

def get_nth_byte(hex_string, n):
	return hex_string[n*2:(n*2)+2]

	

def attack():
	
	bad_string = '00'*16
	ciphertext = oracle_encrypt(bad_string)
	ciphertext = '00'*16 + ciphertext
	
	# First block is all 0s
	# Second block is E(K)
	m = oracle_decrypt(ciphertext).json()['error'][19:]
	key = m[32:]
	flag = get_flag(key).json()['plaintext']
	flag = wrap(flag, 2)
	print(to_chr(flag))
	

attack()
