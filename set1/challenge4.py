#Cryptopals 1-4

def xor(buf_a, buf_b):
	#Comes in as two byte arrays
	xor = [a ^ b for (a,b) in zip(buf_a, buf_b)]
	return bytearray(xor)
	
def score(guess):
	#We want to score a guess. What's the best way to do it?
	
	#Naive mechanism, but works for now. Just give guess a point if it has
	#an english character
	
	target = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	#guess comes in as a bytearray
	score = 0
	for char in guess:
		if chr(char) in target:
			score += 1
	
	return score
	
def hex_to_bytes(string):
	return bytearray.fromhex(string)

def read_challenge():
	# Takes in a challenge file and returns the entries as
	# a list
	
	challenge_file = 'challenge4input.txt'
	with open(challenge_file) as f:
		lines = f.read().splitlines()
	
	return lines

def score_hex(hex_line):
	# Takes in a hex input, and returns the high scoring ones after xoring 
	
	
	# Templates,  pre-processing
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
	options = []	
	b_string = hex_to_bytes(hex_line)
	
	
	for char in alphabet:
		#generate the keystream
		char_stream = bytearray([char]*len(b_string))
		
		guess = xor(b_string, char_stream)
		guess_score = score(guess)
		options.append((guess, guess_score))
	
	sorted_guesses = sorted(options, key=lambda x: x[1], reverse=True)
	high_score = sorted_guesses[0][1]
	
	#Get all the guesses with the high score
	candidates = [(guess[0], guess[1]) for guess in sorted_guesses if guess[1] == high_score]
	return(candidates)

def write_candidates(candidate_set):
	out_file = "candidates4.txt"
	with open(out_file, 'w') as f:
			for item in candidate_set:
				for candidate in item:
					try:
						f.write('%s, %s\n' % ((bytes(candidate[0]).encode()), candidate[1]))
					except UnicodeDecodeError:
						continue
		

def sample():
	# Go through the lines, score them
	hex_lines = read_challenge()
	
	candidate_set = []
	
	for hex_line in hex_lines:
		candidate_set.append(score_hex(hex_line))
	
	write_candidates(candidate_set)

sample()
