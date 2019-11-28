#Cryptopals 3-1


#Sample frequency scoring

def xor(buf_a, buf_b):
	#Comes in as two byte arrays
	xor = [a ^ b for (a,b) in zip(buf_a, buf_b)]
	return bytearray(xor)

def hex_to_bytes(string):
	return bytearray.fromhex(string)
	
def score(guess):
	#We want to score a guess. What's the best way to do it?
	
	#Naive mechanism
	
	target = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	#guess comes in as a bytearray
	score = 0
	for char in guess:
		if chr(char) in target:
			score += 1
	
	return score

def sample():
	string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	
	b_string = hex_to_bytes(string)
	
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	options = []
	for char in alphabet:
		#generate the keystream
		char_stream = bytearray([char]*len(b_string))
		guess = xor(b_string, char_stream)
		guess_score = score(guess)
		options.append((guess, guess_score))
	
	return sorted(options, key=lambda x: x[1], reverse=True)
	
print(sample())
