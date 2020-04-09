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

def guess_last_byte(m, known):
	'''
	m is a n byte block
	we want find m' such that E(m + m') == c
	'''
	# Get the padded block
	c = get_nth_block(m, 0)
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

def slide_guess():
	prepend = '79656c6c6f77207375626d6172696e' # 15 byte block to start with
	flag = []
	
	# Loop skeleton goes here
	
	flag_byte = guess_last_byte(prepend, flag)
	flag.append(flag_byte)

	prepend = prepend[0:28]
	flag_byte = guess_last_byte(prepend, flag)
	flag.append(flag_byte)
	
	return flag
	

def naive_brute_force(message):
	'''
	The idea is because it's ECB, we can brute force each byte at a time, which makes it only
	256 * 16 * 4 = 16384, 10^5
	for brute-force complexity. 
	'''
	
	prepend = message #Prepend 15 bytes, the 16th byte will be the next byte of the flag
	answer = []
	for i in range(0, 15):
		print("Prepend message: " + prepend)
		# Get the first 16 bytes of the ciphertext
		c = ping_oracle(prepend).json()['ciphertext'][0:32]

		# Identify the last byte
		target = c[30:]
		
		# Guess what the 16th byte was
		p_byte = guess(prepend, target, 30)

		# Add the byte to the list
		answer.append(p_byte)

		# Slide the prepend backwards
		slide = prepend + p_byte
		prepend = slide[4:]

	answer = [chr(int(x, 16)) for x in answer]
	print(answer)
	return answer	
		
	
	
	

	
	
answer = slide_guess()
print(answer)
