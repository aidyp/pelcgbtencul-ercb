#Cryptopals 1-1

def hex_to_64(hex_string):
	raw     = hex_string.decode("hex")
	sixfour = raw.encode("base64")
	return sixfour


#Sample usage
def sample():
	string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	return hex_to_64(string)

print(sample())
