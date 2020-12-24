#Challenge 6 -- the "qualifying" set

import functions.analysisfunctions as af
import functions.cryptofunctions as cf
import functions.iofunctions as io
import challenge4 as c4
from itertools import izip_longest


# Notes #

# Pretty sure keysize is 5, now just have to find the key properly #


def hamming_keysize(target_string, keysize):
	# Function returns the hamming distance between the target string and the guessed key length #
	
	# Seperate the string into blocks of keysize #
	blocks = [target_string[i:i+keysize] for i in range(0, len(target_string), keysize)]
	
	index = 0
	distances = []
	while True:
		try:
			# Take the first two chunks and compute the normalised edit distance #
			left = blocks[0]
			right = blocks[1]
			distance = cf.hamming(left, right)
			if distance == -1:
				raise Exception()
			distances.append(distance)
			
			
			del blocks[0]
			del blocks[1]
		except Exception as e:
			return sum(distances)/len(distances)
			

def read_challenge():
	challenge = io.read_file('input/challenge6.txt')
	return io.string_to_bytes(challenge, 'base64')
	
	
def find_key_length(target_string):
	
	#Make tuples of keylength vs hamming distance
	key_hamming_tuples = []
	for i in range(2, 41):
		guess = i
		distance = hamming_keysize(target_string, i)
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
	
	# Re writing transposition to double check it's being done correctly #
	transposed = [bytearray(t) for t in izip_longest(*target_by_block, fillvalue=0)]
	
	
	return transposed


# Need to work on this #

def solve_block(transposed_block):
	# Solve Block is an extension of Challenge 4, and will follow the same logic #
	
	alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'\" :;"
	scores = []
	#Try each character against the block
	for char in alphabet:
		
		# xor the character key with the alphabet #		
		guess = cf.xor_encrypt(transposed_block, bytearray(char))
		
		# Record the score #
		score = af.measure_of_english(guess)
		scores.append((char, score))
		
	
	sorted_guesses = sorted(scores, key=lambda x: x[1], reverse=True)
	return sorted_guesses


# Dummy function for testing little things as needed #
def testing():
	challenge = read_challenge()
	blocks = split_string_by_block(challenge, 29)
	t_blocks = transpose_blocks(blocks)
	
	solutions = [0]*len(t_blocks)
	for i in range(0, len(solutions)):
		solutions[i] = solve_block(t_blocks[i])
	
	return solutions
	

