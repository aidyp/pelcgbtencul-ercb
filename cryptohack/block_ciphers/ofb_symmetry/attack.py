import requests
import codecs

def get_flag():
	base_url = 'https://aes.cryptohack.org/symmetry/encrypt_flag/'
	r = requests.get(base_url)
	return r.json()['ciphertext']


def encrypt(plaintext, iv):
	base_url = 'https://aes.cryptohack.org/symmetry/encrypt/'
	ping_url = base_url + plaintext + '/' + iv + '/'
	r = requests.get(ping_url)
	print(r.text)
	return r.json()['ciphertext']

def xor(a, b):
	'''
	xor two equally sized hex strings
	'''
	return "".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(a, b)])

def to_chr(hex_string):
	decode_hex = codecs.getdecoder("hex_codec")
	return decode_hex(hex_string)[0]
	

def attack():
	c = get_flag()
	iv = c[0:32]
	enc_flag = c[32:64]
	enc_flag2 = c[64:96]
	enc_iv = encrypt('00'*32, iv)
	
	enc_iv_1 = enc_iv[0:32]
	enc_iv_2 = enc_iv[32:64]
	
	flag_1 = xor(enc_iv_1, enc_flag)
	flag_2 = xor(enc_iv_2, enc_flag2)

	print(to_chr(flag_1 + flag_2))
	
	

attack()
