# Crypto Functions #

"""
This file contains low level cryptographic functions
"""



# xor(buf_a, buf_b)
# IN : two equal length byte arrays
# OUT: one byte array where each element is the XOR result of the two inputs
def xor(buf_a, buf_b):
	xor = [a ^ b for (a,b) in zip(buf_a, buf_b)]
	return bytearray(xor)


# hamming(bytes1, bytes2)
# IN : two equal length byte arrays
# OUT: the normalised hamming distance between the two input byte arrays
# ERR: -1 if the byte arrays are not of equal length
def hamming(bytes1, bytes2):
	hamming = 0
	
	#Special case if they're not the same length
	if len(bytes1) != len(bytes2):
		return -1
		
	for i in range(0, len(bytes1)):
		#XOR the two byte values
		xor = bytes1[i] ^ bytes2[i]
		
		#Count the number of ones
		binary = bin(xor)[2:]
		ones = binary.count('1')
		hamming += ones
	
	return (hamming / float(len(bytes1)))

# xor_encrypt(message, key)
# IN : message, key as two bytearrays
def xor_encrypt(message, key):
	if len(key) >= len(message):
		return xor(message, key[0:len(message)])
	else:
		extended_key = make_xor_key(key, len(message))
		return xor(message, extended_key)

# make_xor_key(message, key)
# IN : message, key as two bytearrays where len(key) < len(message)
# OUT: key of appropriate length
def make_xor_key(key, message_length):
	repeats = message_length / len(key) + 1
	return bytearray((key * repeats)[0:message_length])
	
