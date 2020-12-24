import pkcs11
import os
lib = pkcs11.lib(os.environ['PKCS11_MODULE'])
token = lib.get_token(token_label="Token-1")


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
                  

with token.open(user_pin='12345') as session:
	
