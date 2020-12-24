#Cryptopals 1-2

def xor(buf_a, buf_b):
	#Comes in as two byte arrays
	xor = [a ^ b for (a,b) in zip(buf_a, buf_b)]
	return bytearray(xor)
	


def hex_to_bytes(string):
	return bytearray.fromhex(string)

def bytes_to_hex(byte_array):
	#Comes in as a byte array
	return bytes(byte_array).encode('hex')

#Sample usage
def sample():
	message = "1c0111001f010100061a024b53535009181c"
	key     = "686974207468652062756c6c277320657965"
	m_bytes = hex_to_bytes(message)
	k_bytes = hex_to_bytes(key)
	c_bytes = xor(m_bytes, k_bytes)
	
	cipher  = bytes_to_hex(c_bytes)
	print(cipher)
	
	

sample()
