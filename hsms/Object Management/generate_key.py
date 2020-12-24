import pkcs11 as pk
import os


#Open a session on the sample token
lib = pk.lib(os.environ['PKCS11_MODULE'])
token = lib.get_token(token_label="Token-1")

#Want to open with write being true - as we're making a new key!
with token.open(rw=True, user_pin='12345') as session:
	print(session)
	
	
	
	
	#Generate a symmetric key to store.
	#https://python-pkcs11.readthedocs.io/en/latest/api.html#pkcs11.Session.generate_key#
		
	#Parameter build
	
	kparams = {}
	kparams['key_type']     = pk.KeyType.AES #keytype
	kparams['key_length']   = 256            #int
	kparams['id']           = b'00000002'    #bytes
	kparams['label']        = 'myfirstkey'  #string
	kparams['store']        = True           #Bool
	
	
	#Optional parameters
	
	#key_capabilities     =    #pk.MechanismFlag
	#key_mechanism_params =    #pk.Mechanism
	#template             =    #dictionary of Attributes
	
	
	#PKCS11 requires you check your own errors
	#Here we check if they key already exists
	
	try:
		check_key = session.get_key(label=kparams['label'])
		print("This key already exists!")
	except pk.NoSuchKey:
		#Couldn't find the key you want to make, so it's okay to make a new one
		new_key = session.generate_key(**kparams)
		
		#This is the key object handle
		print(key)
	except pk.MultipleObjectsReturned:
		pass
	
	
	
	
	
	
	#Finding the key again
	try:
		found_key = session.get_key(label=kparams['label'])
		print(found_key)
	except NoSuchKey:
		pass
	except MultipleObjectsReturned:
		pass

	#Session is automatically closed when we exit from the with block
	
