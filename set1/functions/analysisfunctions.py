# Analysis functions #

"""
This file contains functions for analysis on plaintext, e.g frequency analysis
"""

# measure_of_english(source) #
# IN : takes in a byte array for analysis
# OUT: returns a linear proximity score as a percentage
def measure_of_english(source):
	english = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!?,.;:\'\" "
	score = 0
	for byte in source:
		try:
			if chr(byte) in english:
				score += 1
		except:
			pass
	return (score / float(len(source)))
	
