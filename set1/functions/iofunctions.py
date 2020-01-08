# Cryptopals io functions

# hex_to_64(hex_string) #
# IN : Takes in a hex string
# OUT: Returns the string encoded as base64
def hex_to_64(hex_string):
	raw     = hex_string.decode("hex")
	sixfour = raw.encode("base64")
	return sixfour

# bytes_to_string(byte_array, encoding) #
# IN : Takes in an array of raw bytes, and an encoding mechanism
# OUT: Returns an encoded string
def bytes_to_string(byte_array, encoding=None):
	return bytes(byte_array).encode(encoding)

# read_file_by_line(filename) #
# IN : Takes the location of a file as a string
# OUT: Returns a list of lines
def read_file_by_line(filename):	
	with open(filename) as fd:
		lines = fd.read().splitlines()	
	return lines

# read_file(filename) #
# IN : Takes in a file location
# OUT: Returns the file's contents as a string
def read_file(filename):
	with open(filename) as fd:
		out = fd.read()	
	return out

# string_to_bytes(string, encoding) #
# IN : takes in a string (optionally an encoding mechanism if the string is encoded)
# OUT: returns an array of raw bytes
def string_to_bytes(string, encoding=None):
	try:
		return bytearray(string.decode(encoding))
	except TypeError:
		return bytearray(string)
