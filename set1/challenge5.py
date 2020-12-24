#Repeating key XOR
import functions.cryptofunctions as cf
import functions.iofunctions as io

def challenge5(msg, key):
		
	# Convert to bytes #
	b_msg = io.string_to_bytes(msg)
	b_key = io.string_to_bytes(key)
	
	# Encrypt #
	ciphertext = cf.xor_encrypt(b_msg, b_key)
	
	# Output as hex #
	out = io.bytes_to_string(ciphertext, 'hex') 
	return out
	


msg = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
print(challenge5(msg, key))
	
