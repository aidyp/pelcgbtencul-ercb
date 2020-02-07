	# Comes in as an input array, looks like
	# [in0 , in1 , ... , in15]
	# aes spefication
	# s[r, c] = in[r + 4c]
def copy_to_state_array(input_byte_array):
	
	state_array = [ [bytes(0) for _ in range(4)] for _ in range(4) ]
	
	for r in range(4):
		for c in range(4):
			state_array[r][c] = input_byte_array[r + 4*c]
	
	return state_array

def add_bytes(byte1, byte2):
	xor = [a ^ b for (a,b) in zip(byte1, byte2)]
	return bytearray(xor)

def to_hex(byte_array):
	return "".join("\\x%02x" % b for b in byte_array)
	
def xtime(byte):
	b = byte[0]
	if (b & 0x80):
		return (((b << 1) ^ 0x1B) & 0xff)
	else:
		return (b << 1)
	

	
