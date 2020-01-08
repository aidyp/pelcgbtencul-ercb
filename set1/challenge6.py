#Challenge 6 -- the "qualifying" set


#KEYSIZE is the guessed length of the key
#For each KEYSIZE, take the first KEYSIZE worth of bytes and the second, and find the edit distance between them

def guess_keysize(target_string, guess):
	
	#Want to guess a keysize. Start with a fixed amount 
	keysize_guess = guess
	
	#Take the first KEYSIZE bytes and the second KEYSIZE bytes, get hamming
	left = target_string[0:(keysize_guess)]
	right = target_string[keysize_guess:(2*keysize_guess)]
	dist = (hamming(left, right)) / float(keysize_guess)
	return dist
	
def find_key_length(target_string):
	
	#Make tuples of keylength vs hamming distance
	key_hamming_tuples = []
	for i in range(2, 41):
		guess = i
		distance = guess_keysize(target_string, i)
		key_hamming_tuples.append((guess, distance))
	
	#Return a sorted version
	sorted_guesses = sorted(key_hamming_tuples, key=lambda x: x[1])
	return sorted_guesses
	
def split_string_by_block(target, block_length):
	blocks = []
	i = 0
	while i < len(target):
		try:
			blocks.append(target[i:(i + block_length)])
		except IndexError:
			#This fails on the last block, so just take what's left (big lazy)
			blocks.append(target[i:])
		i += block_length
	
	return blocks

def transpose_blocks(target_by_block):
	target = target_by_block
	#Get in a list of blocks of a fixed length
	length = len(target[0])
	
	transposed = []
	#take the first byte of each block basically
	for i in range(0, length):
		new_block = []
		for block in target:
			try:
				new_block.append(block[i])
			except IndexError:
				#Do nothing, this fails when accessing the last block
				pass
		
		transposed.append(bytearray(new_block))
	return transposed


def score(guess):
	#We want to score a guess. What's the best way to do it?
	
	#Naive mechanism, but works for now. Just give guess a point if it has
	#an english character
	
	target = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'\"1234567890"
	
	#guess comes in as a bytearray
	score = 0
	for byte in guess:
		if chr(byte) in target:
			score += 1			
		else:
			#Idea is to try and punish bad plaintexts
			score = score - 1
	return score
	

def solve_block(transposed_block):
	#Get in a block
	
	alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'\"1234567890"
	options = []
	#Try each character against the block
	for char in alphabet:
		#generate the keystream
		char_stream = bytearray([char]*len(transposed_block))
		
		guess = xor(transposed_block, char_stream)
		guess_score = score(guess)
		options.append((guess, guess_score, char))
	
	sorted_guesses = sorted(options, key=lambda x: x[1], reverse=True)
	high_score = sorted_guesses[0][1]
	
	candidates = [(guess[0], guess[1], guess[2]) for guess in sorted_guesses if guess[1] == high_score]
	return(candidates)


