# ecb oracle attack #

import requests
import time

def ping_oracle(message):
	'''
	Pings the oracle, is guaranteed to get a response, will retry on failure
	'''
	base_url = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'
	ping_url = base_url + message + '/'
	
	#time.sleep(1) #best not go overboard!
	r = requests.get(ping_url)
	while r.json() == None:
		time.sleep(1)
		r = requests.get(ping_url)
	return r

def get_nth_block(m, n):
	resp = ping_oracle(m)
	index = n*32
	nth_block = resp.json()['ciphertext'][index:index+32]
	return nth_block

def to_chr(hex_string):
	return "".join([chr(int(x, 16)) for x in hex_string])



def guess_last_byte(m, known, c):
	'''
	m is a n byte block
	we want find m' such that E(m + m') == c
	'''
	# Unpadded plaintext
	print("Plaintext    : " + m)
	
	# Block we're trying to match
	print("Target block : " + c)
	
	for i in range(0, 16):
		for j in range(0, 16):
			m_guess = ''

			# Add any known bytes
			for k in known:
				m_guess += k
			
			m_dash = hex(i)[2:] + hex(j)[2:]
			m_guess += m_dash
			
			# Query the oracle for the new 0th block
			c_guess = get_nth_block(m + m_guess, 0)		

			if c_guess == c:
				# We've added the correct final byte, can return
				return m_dash

	
	return -1

def slide_guess_one():
	'''
	This finds data about the first block 
	'''
	prepend = '79656c6c6f77207375626d6172696e' # 15 byte block to start with
	flag = []

	
	for i in range(0, 15):
		target = get_nth_block(prepend, 0)
		flag_byte = guess_last_byte(prepend, flag, target)
		flag.append(flag_byte)

		# Update the prepend
		index = (15 - i) * 2 - 2

		prepend = prepend[0:index]
	
	return flag
		

def slide_guess_two():
	prepend = '63727970746f7b70336e3675316e35' # first 15 bytes of the flag
	
	# Target block is the 2nd set of 16 bytes

	# Pad for alignment
	pad = prepend + 'ff'

	c = get_nth_block(pad, 1)
	flag_byte = guess_last_byte(prepend, [], c)
	print(flag_byte)
	
def slide_guess_three():
	'''
	We know the first 15 bytes of flag 1, so we can try and guess the first byte of flag 2
	'''
	prepend = '63727970746f7b70336e3675316e35'
	known = []
	
	# Second block of ciphertext has one byte of flag2

	c = get_nth_block(prepend, 1)

	prep = prepend[2:] + '5f'
	flag_byte = guess_last_byte(prep, known, c)
	known.append(flag_byte)
	print(flag_byte)
	
	for i in range(0, 14):
		prep = prep[2:]
		c = get_nth_block(prep, 1)
		flag_byte = guess_last_byte(prep, known, c)
		known.append(flag_byte)
		print(flag_byte)
	

hexy = ['63', '72', '79', '70', '74', '6f', '7b', '70', '33', '6e', '36', '75', '31', '6e', '35', '5f', '68', '34', '37', '33', '5f', '33', '63', '62', '7d']
init_flag = "".join(hexy)
print(to_chr(hexy))


