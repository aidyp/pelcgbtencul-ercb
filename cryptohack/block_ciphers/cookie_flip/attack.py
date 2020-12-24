import requests
from datetime import datetime, timedelta
import codecs
import time

def get_cookie():
	base_url = 'https://aes.cryptohack.org/flipping_cookie/get_cookie/'
	r = requests.get(base_url)
	return r.json()['cookie']

def generate_hex_cookie():
	expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
	cookie = f'admin=False;expiry={expires_at}'.encode()
	return cookie.hex()

def get_flag(iv, cookie):
	base_url = 'https://aes.cryptohack.org/flipping_cookie/check_admin/'
	ping_url = base_url + cookie +'/' + iv + '/'
	r = requests.get(ping_url)
	return r.json()

def flip_hex_cookie(cookie):
	# First let's determine that we know _which_ bytes to flip
	print(to_chr(cookie[12:22]))
	low = 12
	high = 22
	
	# True is one fewer letter
	cookie = cookie[0:high - 2] + cookie[high:]
	print(to_chr(cookie))

	# Now we need to change 4 characters, or 8 bytes
	
def xor(a, b):
	'''
	xor two equally sized hex strings
	'''
	return "".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(a, b)])

def to_chr(hex_string):
	decode_hex = codecs.getdecoder("hex_codec")
	return decode_hex(hex_string)[0]



def attack():
	# Get the cookie first
	cookie = get_cookie()
	iv = cookie[0:32]

	# Examine the ideal cookie
	hex_cookie = generate_hex_cookie()
		
	# We want to change the IV, with the following bytes
	# Idea is  we want to have
	# "False" + IV + NEW_IV = "True;"
	# NEW_IV = "False" + "True;" + IV

	modify = xor("False".encode().hex(), "True;".encode().hex())
	modify = xor(modify, iv[12:22])
	
	# Change bytes 12-22
	
	new_iv = iv[0:12] + modify + iv[22:]		
	
		
	encrypted_cookie = cookie[32:]
	print(get_flag(new_iv, encrypted_cookie))
	
	
attack()
	

