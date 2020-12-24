import requests
import time
import codecs

def get_ciphertext_cbc():
	'''
	Pings the oracle, is guaranteed to get a response, will retry on failure
	'''
	base_url = 'https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/'
	#time.sleep(1) #best not go overboard!
	r = requests.get(base_url)
	return r.json()['ciphertext']

def decrypt_ecb(c):
	base_url = 'https://aes.cryptohack.org/ecbcbcwtf/decrypt/'
	c = c + '/'
	r = requests.get(base_url + c)
	return r.json()['plaintext']

def xor(a, b):
	'''
	xor two equally sized hex strings
	'''
	return "".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(a, b)])

def to_chr(hex_string):
	decode_hex = codecs.getdecoder("hex_codec")
	return decode_hex(hex_string)[0]

def attack():
	'''
	Attack is not too tricky!
	'''
	c = get_ciphertext_cbc()
	iv = c[0:32]
	c_1 = c[32:64]
	c_all = c[32:]
	
	m = decrypt_ecb(c_all)
	f_1 = xor(m[0:32], iv)
	f_2 = xor(m[32:64], c_1)
	print(to_chr(f_1) + to_chr(f_2))

attack()
