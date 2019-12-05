#Repeating key XOR


def xor(buf_a, buf_b):
	#Comes in as two byte arrays
	xor = [a ^ b for (a,b) in zip(buf_a, buf_b)]
	return bytearray(xor)

def hex_to_bytes(string):
	return bytearray.fromhex(string)

def make_xor_key(buf_a, key):
	
	#Get the length and repeating length
	length = len(buf_a)
	repeat = length / len(key) + 1
	repeated_key = bytearray((key * repeat)[0:length])
	#print(repeated_key)
	
	return repeated_key
	
def encrypt(message, key):
	
	#Convert the message and key into buffers. 
	
	buf_msg = bytearray(message)
	buf_key = make_xor_key(buf_msg, key)
	
	#Xor the two and return it
	#print(message)
	return xor(buf_msg, buf_key)

def sample():

	msg = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
	key = "ICE"
	
	ciphertext = encrypt(msg, key)
	
	return bytes(ciphertext).encode("hex")
	
def menu():
	print("****************")
	print("XOR keystream v1")
	filename = raw_input("Filename of the input file: ")
	key      = raw_input("Enter the key: ")
	
	#Read in the file
	with open(filename, 'r') as fd:
		msg = fd.read()
	
	#Encoding
	msg = msg.decode("base64")
	
	ciphertext = encrypt(msg, key)
	fd.close()
	
	with open(("XORD_" + filename), 'w') as fd:
		fd.write(ciphertext)
	fd.close()

main = menu()
	
