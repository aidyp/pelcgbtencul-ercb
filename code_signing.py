import pkcs11
import os

#PKCS#11 API codes
api_codes = {'LABEL': 3}



#Code signing primitive



#Initialise the PKCS#11 library
lib = pkcs11.lib(os.environ['PKCS11_MODULE']) 


#Get the hardware token
token = lib.get_token(token_label='Token-1')



input_data = b'BABY GIVE ME A SIGN'

#Open a session
with token.open(user_pin='12345') as session:
	
	#Get the signing key handles
	try:
		pub, priv = session.get_objects(attrs={pkcs11.Attribute.LABEL:'testrsa1'})
	except pkcs11.NoSuchKey:
		print("Key doesn't exist")
		pass
	except pkcs11.MultipleObjectsReturned:
		print("More than one key exists with this label")
		pass
	except ValueError:
		print("!!!")
		pass
	
	
	#Sign with the public
	signature = priv.sign(input_data)
	
	#Verify with the private
	assert pub.verify(input_data, signature)
	
	#Modify the input data
	modified_data = b'BABY GIVE ME A SINE'
	
	#Verify with the private
	try:
		assert pub.verify(modified_data, signature)
	except AssertionError:
		print("This signature doesn't match the data")
		pass
	
	

	





