"""
== README ==

This snippet examines how to log in to our virtual HSM.

"""


#Import the relevant libraries
#1. pkcs11 is the python library to interact with PKCS11 API
#2. os is the library to access environment variables
import pkcs11 as pk
import os

#Initialise the PKCS#11 library
lib = pk.lib(os.environ['PKCS11_MODULE'])
 
#environment variable maps to /usr/local/lib/softhsm/libsofthsm2.so
token = lib.get_token(token_label='Token-1')



#Here's some sample data
data = b'INPUT DATA'


#Open a session on the token
with token.open(user_pin='12345') as session:
	print("Session opened successfully!")
	
	#Now we can start doing some "work" on the HSM
	
	
	# AES Example # 
	
	#Make a key
	key = session.generate_key(pk.KeyType.AES, 256)
	
	#Get an Initialisation Vector
	iv = session.generate_random(128)
	
	#Encrypt
	ciphertext = key.encrypt(data, mechanism_param=iv)
	
	#Decrypt for correctness
	plaintext = key.decrypt(ciphertext, mechanism_param=iv)
	
	
	
	#The last two printed lines should be the same
	print(ciphertext)
	print(plaintext)
	print(data)
	
	
