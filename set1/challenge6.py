#Challenge 6 -- the "qualifying" set

import functions.analysisfunctions as af
import functions.cryptofunctions as cf
import functions.iofunctions as io
import challenge4 as c4
from itertools import izip_longest


# Notes #

# Pretty sure keysize is 5, now just have to find the key properly #


def hamming_keysize(target_string, guess):
	# Function returns the hamming distance between the target string and the guessed key length#
	
	#Split the string by keysize
	left_1 = target_string[0:guess]
	right_1 = target_string[guess:(guess*2)]
	left_2 = target_string[(guess*2):(guess*3)]
	right_2 = target_string[(guess*3):(guess*4)]
	
	edit_1 = cf.hamming(left_1, right_1)
	edit_2 = cf.hamming(left_2, right_2)
	
	return (edit_1 + edit_2 / float(2))

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
	
	alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'\"0123456789"
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
	blocks = split_string_by_block(challenge, 5)
	t_blocks = transpose_blocks(blocks)
	
	solutions = [0]*len(t_blocks)
	for i in range(0, len(solutions)):
		solutions[i] = solve_block(t_blocks[i])
	
	return solutions
	

