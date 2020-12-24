import pkcs11
import os
lib = pkcs11.lib(os.environ['PKCS11_MODULE'])
token = lib.get_token(token_label="Token-1")

#Find the key

attribute_dict = {
                  'CLASS'           :0,
                  'TOKEN'           :1,
                  'PRIVATE'         :2,
                  'LABEL'           :3,
                  'APPLICATION'     :16,
                  'VALUE'           :17,
                  'SIGN'            :264,
                  'VERIFY'          :266,
                  'OBJECT_ID'       :18,
                  'CERTIFICATE_TYPE':128,
                  'ISSUE'           :129,
                  }
                  
#Probably best to build a class to do all of this, but that's an idea for future development. The goal now is to write a signing primitive using PKCS#11

with token.open(user_pin='12345') as session:
	
	print(session)
	
	try:
		#3 -> LABEL. Might be best to have constants mapped, when you need to find something
		pub, priv = session.get_objects(attrs={3:"testrsa1"})
		print("Key handles retrieved successfully")
		
		
		#Exploring ways to understand the key handles just found
		#Use the __getitem__() method (accesses indexed attributes!) -> New Python syntax
		print(pub[attribute_dict['VERIFY']])
		print(priv[attribute_dict['SIGN']])
	except pkcs11.NoSuchKey:
		pass
	except pkcs11.MultipleObjectsReturned:
		pass
	except ValueError:
		print("Not sure what this is")
		pass
		
		

