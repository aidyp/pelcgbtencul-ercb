#Cryptopals 1-4
import functions.cryptofunctions as cf
import functions.iofunctions as io
import functions.analysisfunctions as af


def explore_xor_char(entry):
	# Takes in a single bytearray, and returns an ordered list of the scores #
	
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
	scores = []	
	
	for char in alphabet:
		
		# xor the character key with the alphabet #		
		guess = cf.xor_encrypt(entry, bytearray(char))
		
		# Record the score #
		score = af.measure_of_english(guess)
		scores.append((char, score))
		
	
	sorted_guesses = sorted(scores, key=lambda x: x[1], reverse=True)
	return sorted_guesses


def load_challenge():
	challenge = io.read_file_by_line('input/challenge4input.txt')
	return challenge


def rank_lines(challenge):
	
	# Each line in the challenge has a "best" xor #
	pairs = []
	
	for line in challenge:
		# Get the character/score table #
		b_line = io.string_to_bytes(line, 'hex')
		char_guesses = explore_xor_char(b_line)
		
		# Pick the best pair #
		best_pair = char_guesses[0]
		pairs.append([best_pair, line])
	
	# Rank the pairs #
	ranked_pairs = sorted(pairs, key=lambda x: x[0][1], reverse=True)
	
	return ranked_pairs
	
def decrypt_candidate(candidate):
	
	key = candidate[0][0]
	ciphertext = candidate[1]
	
	plaintext = cf.xor_encrypt(io.string_to_bytes(ciphertext, 'hex'), io.string_to_bytes(key))
	return plaintext
